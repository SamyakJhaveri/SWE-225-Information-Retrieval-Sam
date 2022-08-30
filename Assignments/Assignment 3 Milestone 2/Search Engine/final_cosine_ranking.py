# With reference to: 
# 1. https://alliescomputing.com/knowledge-base/christmas-carol-search-using-tf-idf-and-cosine-similarity

# Imports
from nltk.stem import SnowballStemmer
import re
import ast
import math
import numpy as np
# SnowballStemmer object
ss = SnowballStemmer(language = 'english')

corpus_length = 55393 # hardcoded for now

def calculate_cosine_similarity(stemmed_query, tf_idf, tfidf_dict_qry):
    print(tf_idf)
    print("stemmed_query", stemmed_query)

    dot_product = 0
    qry_mod = 0
    doc_mod = 0
    index = 0
    cos_sim = []
    for keyword in stemmed_query:
        print("keyword:", keyword)
        for i in (tf_idf[keyword]):
            
            dot_product += tfidf_dict_qry[keyword] * i
            doc_mod += i * i
        
        qry_mod += tfidf_dict_qry[keyword] * tfidf_dict_qry[keyword]
        
            
    qry_mod = np.sqrt(qry_mod)
    doc_mod = np.sqrt(doc_mod)

    denominator = qry_mod * doc_mod

    cos_sim = dot_product/denominator
    return cos_sim

def stemm_query(queries):
    '''
    Stems the query into a list of stemmed query words
    Input: Query Words <type: List<String>>
    Output: Stemmed Query Words <type: List<String>>
    '''
    stemmed_query = []
    for query_word in queries:
        query_word = query_word.lower() # 'create', 'papers'
        stemmed_query.append(ss.stem(query_word)) # ['create', 'paper']

    return stemmed_query

def find_document_tf_values(values):
    '''
    Calculates and Returns Term-Frequency values
    Input: values <type: List<List<int>>>
    Output: document tf values <type: List<float>>
    '''
    document_tf_values = []
    for value in values:
        document_tf_values.append(value[0])
    return document_tf_values


def findQuery(word):
    '''
    Takes query as input, stems it, and searches for the respective
    stemmed term in results dictionary.
    Once the corresponding entry of the stemmed term is found, its 
    Term-Frequency, Document-Frequency and index at whcih its URL 
    is present is extracted form the main dictionary.
    Using al this information, the cosine similarity of the query w.r.t 
    the most relevant documents (the ones that rank higher in their tf-idf score)
    are calculated.
    Input: One of the Stemmed Query Words <type: String>
    Output: 
        - Word Term-Frequency <type: List<float>>
        - Document URL Indexes <type: List<String>>
        - Document-Frequency <type: Integer>
    '''

    file_url = ''
    url_string = "latest data/IndexData_new/" + word[0] + ".txt"
    # 'latest data/IndexData_new/c.txt' for 'crux'
    with open(url_string, 'r') as f:
           content = f.readlines()
    f.close

    document_frequency = 0

    query_string = '"' + word + '"'
    # query_string = '"crux"'

    document_tf_values = []
    line_number = 0
    for line in content:
        line_number += 1
        if query_string in line:
            break
        else:
            continue
    
    dictionary_of_line = ast.literal_eval(line)
    
    document_frequency = len(dictionary_of_line[word])
    # document_frequency for 'curx': 3       
    
    document_url_index = dictionary_of_line[word].keys()
    # document_url_index for 'crux': ['16165', '18410', '20538']
    
    values = dictionary_of_line[word].values()          
    # values for 'crux' = [[0.0, [54378], [0.0, [11303], [0.0, [2070]]
    
    document_tf_values = find_document_tf_values(values)      
    # document_tf_values for 'crux' = [0.0, 0.1, 0.2]
    
    idf_doc =  math.log(float(corpus_length) / document_frequency)
    tf_idf_score = []
    for i in range(document_frequency):
        tf_idf_score.append(document_tf_values[i] * idf_doc)

    return document_frequency, document_url_index, document_tf_values, tf_idf_score    


def main():
    query = 'crux puppets'

    queries = query.split(' ')
    # queries = ['crux', 'puppets']

    stemmed_query = stemm_query(queries)
    # stemmed_query = ['crux', 'puppet']
    tf_idf = {}
    idf_dict = {}
    query_norm_tf = {}
    idf_dict_qry = {}
    tfidf_dict_qry = {}
    # tf_idf = {'crux': [ ], 'puppet' : []}
    for w in stemmed_query:
        # 'crux'
        document_frequency, document_url_index, document_tf_values, tf_idf[w] = findQuery(w)
        
        query_norm_tf[w] = stemmed_query.count(w) / float(len(stemmed_query))
        idf_dict_qry[w] = (math.log(float(corpus_length) / document_frequency))
        tfidf_dict_qry[w] = query_norm_tf[w] * idf_dict_qry[w]

        print(f"Document Frequency of {w}: {document_frequency}") # 3
        print(f"Document URL Index of {w}: {document_url_index}") # ['16165', '18410', '20538']
        print(f"Document TF Values of {w}: {document_tf_values}") # [0.0, 0.0, 0.0] 
        print(f"TF-IDF value of {w} w.r.t documents is: {tf_idf[w]}") 
        print(f"TF-IDF value of {w} w.r.t Query is: {tfidf_dict_qry[w]}")     

    
    print(calculate_cosine_similarity(stemmed_query, tf_idf, tfidf_dict_qry))

if __name__ == "__main__":
    main()

