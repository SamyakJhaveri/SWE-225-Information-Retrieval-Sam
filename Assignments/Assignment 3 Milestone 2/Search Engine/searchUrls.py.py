from ast import And
import glob
import linecache
import math
import json
from operator import le
from nltk.stem import SnowballStemmer
ss=SnowballStemmer(language='english')
import time
def tfidfquery(query):
    d=dict()
    queries=query.split(' ')
    for q in queries:
        q=ss.stem(q.lower())
        if q not in d:
            d[q]=1
        else:
            d[q]+=1
    for q in d:
        d[q]=(1+math.log10(d[q]))*(1+math.log10(len(queries)/d[q]))
    return d
def querynorm(queryDict):
    return math.sqrt(sum(queryDict.values()))
def gettfidfDoc(queryDict):
    tfidfdocDict=dict()
    docnormDict=dict()
    for q in queryDict:
        if(q[0].isdigit()):
            filename="num"
        else:
            filename=q[0]
        filepath = "./IndexDataTfIdf/"
        file=filepath+filename+'.txt'
        start = int(round(time.time() * 1000))
        print(q)
        with open(file,"r") as input_file:
            # while True:
            for content in input_file:
                # content=input_file.readline()
                if not content:
                    break
                textline=content.strip()
                tempObj=json.loads(textline)
                key=list(tempObj.keys())[0]
                if key==q:
                    wordDocDict=tempObj[key]
                    for doc in wordDocDict:
                        if doc in tfidfdocDict:
                            tfidfdocDict[doc]+=(wordDocDict[doc][0]*queryDict[q])
                        else:
                            tfidfdocDict[doc]=(wordDocDict[doc][0]*queryDict[q])
                        if doc in docnormDict:
                            docnormDict[doc]+=wordDocDict[doc][0]
                        else:
                            docnormDict[doc]=wordDocDict[doc][0]
        input_file.close()
        end = int(round(time.time() * 1000))
        print("q:",end-start)
    return tfidfdocDict,docnormDict
def cosinesimilarites(tfidfdocDict,docnormDict,queryDict):
    cosineDict=dict()
    top5Dict=dict()
    querynormalvalue=querynorm(queryDict)
    for doc in tfidfdocDict:
        docnormalvalue=math.sqrt(docnormDict[doc])
        if not (querynormalvalue==0 or docnormalvalue==0):
            value=tfidfdocDict[doc]/(querynormalvalue*docnormalvalue)
            if value!=0.0 or value!=0:
                cosineDict[doc]=value
            # if (value not in top5Dict) and top:
    return cosineDict
def getSortedDocs(query):
    queryDict=tfidfquery(query)
    tfidfdocDict,docnormDict=gettfidfDoc(queryDict)
    cosineDict=cosinesimilarites(tfidfdocDict,docnormDict,queryDict)
    sortedDocDict={k:v for (k,v) in sorted(cosineDict.items(),key=lambda x:x[1],reverse=True)}
    return getDocsFromIds(sortedDocDict)
def getDocsFromIds(sortedDocDict):
    urls=[]
    for docId in sortedDocDict:
        line = linecache.getline('urlmapping.txt', int(docId))
        urls.append(line)
    return urls



