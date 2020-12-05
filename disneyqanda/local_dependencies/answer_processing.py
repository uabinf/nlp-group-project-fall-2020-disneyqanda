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
from local_dependencies.ans_processing.answer import Answer


def answer_processing(question, ranking, df_disney, ans_type):
    print()
    print("Answer Processing")
    
    # POS tag them
    ranking['tokens_pos'] = ranking['tokens_sw_removed'].apply(
            lambda x: nltk.pos_tag(x, tagset='universal')
            )
    # Remove punctuation
    ranking['no_punc'] = ranking['tokens_pos'].apply(
            lambda x: [w[0] for w in x if not w[1] == "."]
            )
    # Remove noun-marked apostrophes
    ranking['no_punc'] = ranking['no_punc'].apply(
            lambda x: [w for w in x if not ((w == "’") or (w == "‘"))]
            )
        
    ranking_ner = ner_tagger(ranking)
    #print(ner_matches)
    
    candidates = get_candidate_answers(question, ranking_ner)
    
    candidates['a_question'] = candidates['question'].apply(
            lambda x: Answer(x))
       
    ans_ranking = rank_candidate(candidates, df_disney, ans_type)
    
    return ans_ranking

        
    
        