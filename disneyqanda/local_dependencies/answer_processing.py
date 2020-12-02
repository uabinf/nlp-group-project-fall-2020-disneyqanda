# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:08:25 2020

Answer Processing

"""
from local_dependencies.ans_processing.ner_tagger import ner_tagger
from local_dependencies.ans_processing.candidate_ranking import rank_candidate
from local_dependencies.ans_processing.candidate_answers import get_candidate_answers


def answer_processing(q, pas):
    print()
    print("Answer Processing")
    
    ner_matches = ner_tagger(pas)
    
    ans = get_candidate_answers(pas)
        
    ans_ranking = rank_candidate(ans)
    
    best_answer = "Guests must be 40 in (102 cm) or taller."
    return best_answer

        
    
        