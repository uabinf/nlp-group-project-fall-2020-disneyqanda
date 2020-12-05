# -*- coding: utf-8 -*-

def get_candidate_answers(question, ranking_ner):
    print("Selecting candidate answers\n")
    
    top50 = ranking_ner.nlargest(50, 'score')
    
    
    # Look for questions matching the words in the question being asked
    top50['words_matched'] = top50['no_punc'].apply(
            lambda x: [w for w in x if w in question.q_no_punc])
    
    top50['words_matched'] = top50['words_matched'].apply(
            lambda x: set(x))
    
    # Count how many words matched
    top50['word_matches'] = top50['words_matched'].apply(
            lambda x: len(x))
       
    
    return top50