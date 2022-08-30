from operator import le
from pymongo import MongoClient
from nltk.stem import SnowballStemmer
ss = SnowballStemmer(language="english")
client = MongoClient()
idfDict = dict()
mydb=client["latestDB"]
myCollection=mydb["tokenTable"]

def searchUrls(query):
    queries = query.split()
    commonDocs = set()

    for q in queries:
        q = q.lower()
        word = ss.stem(q)
        x = myCollection.find_one({ '_id': word})
        curr=set()
        for i in x:
            if i!='_id':
                curr.add(i)
        
        if commonDocs:
            commonDocs = commonDocs.intersection(curr)
        else:
            commonDocs = curr

    return freqScore(commonDocs,queries)

def freqScore(commonDocs,queries):
    scoreDict = dict()
    for doc in commonDocs:
        scoreDict[doc] = 0
    for q in queries:
        word = ss.stem(q)
        x = myCollection.find_one({ '_id': word}) 
        for i in x:
            if i in scoreDict:
                scoreDict[i] += x[i]
    
    temp={k:v for k,v in sorted(scoreDict.items(),key=lambda x:x[1],reverse=True)}
    finalList = []

    for url in temp:
        url=url.replace("\\",".")
        if '#' in url:
            url=url[:url.index('#')]
        if len(finalList) < 5 and url not in finalList:
            finalList.append(url)
        elif len(finalList) == 5:
            break
        else:
            continue
        
    return finalList



    