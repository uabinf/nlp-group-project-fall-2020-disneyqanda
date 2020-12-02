# -*- coding: utf-8 -*-

# Run an answer type ner tagger on the passages
# Can be full ner, simple regex, or hybrid

import pandas as pd

def ner_tagger(psg):
    print("Running NER tagger on passages\n")
    
    df = pd.read_csv("data\qna.txt", sep='\n', header=None)
    df['qnum'] = (df.index - (df.index % 2))//2
    df['i'] = df.index
    df['type'] = df['i'].apply(lambda x: 'Q' if (x % 2) == 0 else 'A') 
    
    
    return "Star Wars"
    