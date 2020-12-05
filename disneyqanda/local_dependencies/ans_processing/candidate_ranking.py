# -*- coding: utf-8 -*-


from .answer_type import a_answer_type
from .key_words import a_key_words

import en_core_web_sm
nlp = en_core_web_sm.load()


def rank_candidate(candidates, df_disney, ans_type):
    print("Ranking candidate answers\n")
        
    # Get the answer type for the candidate answers
    candidates["answer_type"] = candidates["a_question"].apply(
            lambda x: a_answer_type(x, a_key_words(x, df_disney))
            )
    
    candidates['s1'] = candidates['score'].rank(method='max')
    candidates['s2'] = candidates['word_matches'].rank(method='max')
    candidates['s3'] = candidates['answer_type'].apply(
            lambda x: 1 if x == ans_type else 0)
    
    candidates['overall'] = candidates['s1'] + 2*candidates['s2'] + 20*candidates['s3']
    
    
    answer = candidates.nlargest(1, 'overall')
    print("Cosine score:", answer.score.values)
    print("Word matches:", answer.word_matches.values)
    print("Answer's answer type:", answer.answer_type.values)
    
    
    return answer