from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
import glob
import math
import os
from simhash import Simhash
# tf = 1 + log(freq)
ss = SnowballStemmer(language="english")
BATCH_SIZE = 15000
importance ={"title":11,"h1":9,"h2":7,"h3":4,"bold":3,"italic":1} #Extra
simhashes = dict()


def simhash_similarity(data,url):
    data_simhash = Simhash(data)
    for key in simhashes:
        max_hashbit=  max(len(bin(data_simhash.value)), (len(bin(simhashes[key].value))))
        dist = data_simhash.distance(simhashes[key])
        similar=1-dist/max_hashbit
        if(similar > 0.9):
            print("similar found")
            similarFile=open("similar.txt","a")
            similarFile.write(key+'\n')
            similarFile.write(url+'\n')
            similarFile.write('\n')
            return True
    simhashes[url] = data_simhash
    return False


def tokenize(text):
    tokenize_pattern = r"[a-zA-Z0-9]+"
    tokenizer = RegexpTokenizer(tokenize_pattern)
    return tokenizer.tokenize(text)


def getHTMLTags(tags,HTML_tags):
    for x in tags:
        x1 = str(x).split('>')[0]
        x1=x1.split(' ')[0]
        key=x1[2:]
        for t in x:
            temp=[w.lower() for w in tokenize(t.text)]
            for i in temp:
                i=ss.stem(i)
                HTML_tags[key].append(i)


def createIndex(data, invertedIndexDict, curr_doc_index):
    html=data['content']
    soup = BeautifulSoup(html, "html.parser")
    HTML_tags = {"title": [], "h1": [], "h2":[],"h3":[],"bold": [],"italic":[]}
    title,h1,h2,h3=soup.find_all('title'),soup.find_all('h1'),soup.find_all('h2'),soup.find_all('h3')
    bold,italic=soup.find_all('bold'),soup.find_all('italic')
    getHTMLTags([title,h1,h2,h3,bold,italic],HTML_tags)
    body_text=soup.get_text(" ")
    if body_text=="":
        return
    url = data['url']
    if simhash_similarity(body_text, url):
        return
    only_words= [w.lower() for w in tokenize(body_text)]
    for i,word in enumerate(only_words):
        word=ss.stem(word)
        if word in invertedIndexDict:
            if curr_doc_index+1 in invertedIndexDict[word]:
                invertedIndexDict[word][curr_doc_index+1][0] += 1
                invertedIndexDict[word][curr_doc_index+1][1].append(i)
            else:
                invertedIndexDict[word][curr_doc_index+1] = [1,[i]]
        else:
            invertedIndexDict[word] = {curr_doc_index+1 : [1,[i]]}
    for j in HTML_tags:
        for word in HTML_tags[j]:
            if word not in invertedIndexDict:
                output_file=open("./IndexData/ignoredWords.txt","a+")
                output_file.write(word + "\n")
            else:
                if curr_doc_index+1 in invertedIndexDict[word]:
                    invertedIndexDict[word][curr_doc_index+1][0] += importance[j]
                else:
                    output_file=open("./IndexData/ignoredWords.txt","a+")
                    output_file.write(word + "\n")
    stemmed=set()
    for x in only_words:
        stemmed.add(ss.stem(x))
    for i in stemmed:
        invertedIndexDict[i][curr_doc_index+1][0]=math.log10(invertedIndexDict[i][curr_doc_index+1][0])


def dumpIndex(invertedIndexDict):
    lenOfIndex = len(invertedIndexDict)
    for index in invertedIndexDict:
        print("Still in progress! ", index)
        print(lenOfIndex, " records left to process")
        lenOfIndex -= 1
        dumpDict={index:invertedIndexDict[index]}
        if(index[0].isdigit()):
            filename="num"
        else:
            filename=index[0]
        filepath = "./IndexData/"
        file=filepath+filename+'.txt'

        if os.path.exists(file):
            oldfile=filepath+filename+'old.txt'
            os.rename(file,oldfile)# Renamed file to fileold.txt
            flag=False
            with open(file,"a") as output_file:
                with open(oldfile,"r") as input_file:
                    while True:
                        content=input_file.readline()
                        if not content:
                            break
                        textline=content.strip()
                        tempObj=json.loads(textline)
                        key=list(tempObj.keys())[0]
                        if key==index:
                            dumpDict[key] = {**tempObj[key],**dumpDict[index]}
                            output_file.write(json.dumps(dumpDict)+"\n")
                            flag=True
                        else:
                            output_file.write(json.dumps(tempObj)+"\n")
                    if not flag:
                        output_file.write(json.dumps(dumpDict)+"\n")
                input_file.close()
            output_file.close()
            os.remove(oldfile)

        else:
            with open(file,"a") as output_file:
                output_file.write(json.dumps(dumpDict)+"\n")
            output_file.close()
    invertedIndexDict.clear()


def createInvertedIndex():
    invertedIndexDict=dict()
        # invertedIndexDict = {
        #   "word": {
        #       "url1": [score,[pos1,pos2]],
        #       "url2": [score,[pos1,pos2]],
        #   }
            # "word1": {
            # }
        # }
    for curr_doc_index,name in enumerate (glob.glob('F:\Winter 22\IR\Assignment3\developer\DEV\*\*')):
        print("URL: ",curr_doc_index)
        f = open(name)
        data = json.load(f)
        url=data['url']
        urlsFile=open("urlmapping.txt","a")
        urlsFile.write(data['url']+'\n')
        urlsFile.close()
        print(url)
        if urlparse(url).fragment != "":
            if (curr_doc_index+1)%BATCH_SIZE==0 or curr_doc_index+1==55393:
                dumpIndex(invertedIndexDict)
                print("Data dumped!")
                print("Inverted Index length: ",len(invertedIndexDict))
            continue
        createIndex(data, invertedIndexDict, curr_doc_index)
        f.close()

        if (curr_doc_index+1)%BATCH_SIZE==0 or curr_doc_index+1==55393:
            dumpIndex(invertedIndexDict)
            print("Data dumped!")
            print("Inverted Index length: ",len(invertedIndexDict))

if __name__=="__main__":
    createInvertedIndex()