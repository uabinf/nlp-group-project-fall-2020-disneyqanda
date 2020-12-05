# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:08:25 2020

Answer Processing

"""

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

from local_dependencies.ans_processing.ner_tagger import ner_tagger
from local_dependencies.ans_processing.candidate_answers import get_candidate_answers
from local_dependencies.ans_processing.candidate_ranking import rank_candidate


def answer_processing(question, pas):
    print()
    print("Answer Processing")
    
    # For now, read the Disney q and a data here
    df = pd.read_csv("data\qna.txt", sep='\n', header=None, names=['text'])
    df['qnum'] = (df.index - (df.index % 2))//2
    df['i'] = df.index
    df['type'] = df['i'].apply(lambda x: 'Q' if (x % 2) == 0 else 'A') 
    
    # Tokenize all questions and answers
    df['tokens'] = df['text'].apply(lambda x: word_tokenize(x))
    # Remove stopwords
    df['tokens_sw_removed'] = df['tokens'].apply(
            lambda x: [w.lower() for w in x if not w.lower() in stop_words]
            )
    # POS tag them
    df['tokens_pos'] = df['tokens_sw_removed'].apply(
            lambda x: nltk.pos_tag(x, tagset='universal')
            )
    # Remove punctuation
    df['no_punc'] = df['tokens_pos'].apply(
            lambda x: [w[0] for w in x if not w[1] == "."]
            )
    df2 = df.copy()
    
    ner_matches = ner_tagger(df)
    #print(ner_matches)
    
    ans = get_candidate_answers(question, df2)
       
    ans_ranking = rank_candidate(ans)
    
    return ans_ranking

        
    
        