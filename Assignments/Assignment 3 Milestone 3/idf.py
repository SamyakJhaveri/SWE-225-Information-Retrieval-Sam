import math
from operator import le
from pymongo import MongoClient
from nltk.stem import SnowballStemmer
ss = SnowballStemmer(language="english")
client = MongoClient()
idfDict = dict()
mydb=client["tfDB"]
myCollection=mydb["tokensTable"]

def searchUrls(query):
    # query = input('Enter the query: ')
    queries = query.split()
    commonDocs = set()
    j=0

    for q in queries:
        word = ss.stem(q)
        x = myCollection.find_one({ '_id': word})
        curr=set()
        for i in x:
            if i!='_id':
                curr.add(i)
        idfDict[word] = math.log(55386/len(curr))
        print(word)
        print(len(curr))
        if commonDocs:
            commonDocs = commonDocs.intersection(curr)
        else:
            commonDocs = curr
    print(commonDocs)
    return tfidfScore(commonDocs,queries)

def tfidfScore(commonDocs,queries):
    scoreDict = dict()
    for doc in commonDocs:
        scoreDict[doc] = 0
    # print(scoreDict)
    for q in queries:
        word = ss.stem(q)
        x = myCollection.find_one({ '_id': word}) 
        for i in x:
            if i in scoreDict:
                scoreDict[i] += (idfDict[word] * x[i])
    
    # temp={k:v for k,v in sorted(scoreDict.items(),key=lambda x:x[1],reverse=True)}
    temp={k:v for k,v in sorted(scoreDict.items(),key=lambda x:x[1])}
    first5Urls = list(temp.keys())[:5]
    finalList = []
    for url in first5Urls:
        finalList.append(url.replace("\\","."))
    
    return finalList



    