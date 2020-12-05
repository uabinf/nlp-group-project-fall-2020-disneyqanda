# -*- coding: utf-8 -*-

import pandas as pd 
def doc_retrieval():
    with open("data/qna.txt", 'r') as f:
        qa = []
        q = ''
        for i, line in enumerate(f):
            if i % 2 == 0:
                q = line[:-1]
            else:
                qa.append([q, line[:-1]])
                q = ''
    doc_df = pd.DataFrame(qa, columns=['question', 'answer'])

    return doc_df

