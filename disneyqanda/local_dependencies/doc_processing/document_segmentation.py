# -*- coding: utf-8 -*-

# Parse it into questions and answers
# Do any processing (tokenization, NER, etc)

from document_retrieval import doc_retrieval
import pandas as pd 

def doc_segmentation(keywords):
    df = doc_retrieval()
    docs = []
    for q in df.iterrows():
        question = q[1]['question']
        for word in keywords:
            if word.lower() in question.lower():
                docs.append([q[1]['question'], q[1]['answer']])
                break
    df = pd.DataFrame(docs, columns = ['question', 'answer'])
    return df

print(doc_segmentation(['smoking']))
