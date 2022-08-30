idf_doc = 1.0+ math.log(float(corpus_lenght) / document_freuency)
            print("this is the tf idf",idf_doc)
            print(document_freuency)
            for doc in document_url_index:
                tf_idf = document_freuency * idf_doc
                #print (tf_idf)
                
                
                
                
    score={}
    for i in range (10000):
        score[1]= cos_sim
                #final[]
        temp={k:v for k,v in sorted(score.items(),key=lambda x:x[1],reverse=True)}
        for url in temp:
            if len(score) < 5 and url not in score:
                score.append(url)
            elif len(score) == 5:
                break
            else:
                continue
            print("temmmp", score)




#Normalized TF for the query string("life learning")
def compute_query_tf(query):
    query_norm_tf = {}
    tokens = query.split()
    for word in tokens:
        query_norm_tf[word] = termFrequency(word , query)
    return query_norm_tf

    
query_norm_tf = compute_query_tf(query)
print(query_norm_tf)
{'life': 0.5, 'learning': 0.5}
In [9]:
#idf score for the query string("life learning")
def compute_query_idf(query):
    idf_dict_qry = {}
    sentence = query.split()
    documents = [doc1, doc2, doc3]
    for word in sentence:
        idf_dict_qry[word] = inverseDocumentFrequency(word ,documents)
    return idf_dict_qry
idf_dict_qry = compute_query_idf(query)
print(idf_dict_qry)
{'life': 1.4054651081081644, 'learning': 1.4054651081081644}
In [10]:
#tf-idf score for the query string("life learning")
def compute_query_tfidf(query):
    tfidf_dict_qry = {}
    sentence = query.split()
    for word in sentence:
        tfidf_dict_qry[word] = query_norm_tf[word] * idf_dict_qry[word]
    return tfidf_dict_qry
tfidf_dict_qry = compute_query_tfidf(query)
print(tfidf_dict_qry)