# -*- coding: utf-8 -*-

# Features for ranking candidate answers
#   - answer type match
#   - pattern match
#   - question keywords
#   - keyword distance
#   - novelty factor
#   - apposition features (adding extra info, like this, to sentence)
#   - punctuation location
#   - sequences of question terms

import en_core_web_sm
nlp = en_core_web_sm.load()


def rank_candidate(ans):
    print("Ranking candidate answers\n")
    
    # Use en_core_web_sm to get named entities in the questions and answers
    ans['doc'] = ans['text'].apply(
            lambda x: nlp(x)
            )
    
    ans['ents'] = ans['doc'].apply(
            lambda x: [(w.text, w.label_) for w in x.ents]
            )
    
    
    
    
    return "good match"