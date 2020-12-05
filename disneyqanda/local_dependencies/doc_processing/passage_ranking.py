# -*- coding: utf-8 -*-

# Rule-based classifiers or supervised ML

# Features for passage ranking:
#   - Number of named entities of the right type in passage
#   - Number of query words in passage
#   - Number of question N-grams in passage
#   - Longest sequence of question words
#   - Rank of the document containing passage

from document_segmentation import doc_segmentation
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def passage_ranking(question, docs):
    print("Ranking passages\n")
    stop_words = set(stopwords.words('english'))
    # Use cosine similarity to rank questions
    # df_cosine = docs.copy()
     
    model = Doc2Vec.load("../../data/doc2vec.model")
   
    # Get the embeddings for the question being asked
    qvec = model.infer_vector(question)
   
    # Get the embeddings for all the questions/answers
    docs['tokens'] = docs['text'].apply(lambda x: word_tokenize(x))
    # Remove stopwords
    docs['tokens_sw_removed'] = docs['tokens'].apply(lambda x: [w.lower() for w in x if not w.lower() in stop_words])
    docs['no_punc'] = docs['tokens_pos'].apply( lambda x: [w[0] for w in x if not w[1] == "."])

    # df2 = docs.copy()
    docs['vector'] = docs['question'].apply(lambda x: model.infer_vector(x.q_no_punc))
   
    # Take the dot product of the vector for the question being asked with
    # that of each candidate question/answer
    docs['score'] = docs['vector'].apply(lambda x: x.dot(qvec))
   
    # Get the top scores (most similar) and put the question #s into a list
    docs = docs.nlargest(10, 'score')
    return docs

question = 'Where can I smoke at disney world'

q = [w[0] for w in word_tokenize(question)]
docs = doc_segmentation(['smoke', 'disney', 'world'])
print(passage_ranking(q, docs))