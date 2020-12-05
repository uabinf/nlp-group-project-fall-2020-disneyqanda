# -*- coding: utf-8 -*-

# Parse it into questions and answers
# Do any processing (tokenization, NER, etc)

import pandas as pd 

def doc_segmentation(doc_df, keywords):
    
    docs = []
    for q in doc_df.iterrows():
        question = q[1]['question']
        for word in keywords:
            if word.lower() in question.lower():
                docs.append([q[1]['question'], q[1]['answer']])
                break
    df_docs = pd.DataFrame(docs, columns = ['question', 'answer'])
    return df_docs
