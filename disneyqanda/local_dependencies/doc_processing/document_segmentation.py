# -*- coding: utf-8 -*-

from document_retrieval import doc_retrieval

def doc_segmentation(keywords):
    df = doc_retrieval()
    docs = []
    for q in df.iterrows():
        question = q[1]['question']
        for word in keywords:
            if word.lower() in question.lower():
                docs.append(q[1]['answer'])
                break
    return docs
