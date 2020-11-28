# -*- coding: utf-8 -*-

# Answer type detection
    # ML classification problem
    # Important features are:
    #   question words and phrases
    #   POS tags
    #   parse features (headwords)
    #   Named Entities
    #   Semantically related words
    # See the keywords selection algorithm slide
    
#from gensim.models import Word2Vec
#import xgboost
#import multiprocessing
#cores = multiprocessing.cpu_count()
#model = Word2Vec(size=256, window=5, min_count=1, workers=cores-2)

  
def get_anstype_features(q):
    return {
        'question': q
        
        
            }
    
def q_answer_type(q):
     if q.q.find("height") > 0:
         a_type = "numeric, height"
     else:
         a_type = "not height"
     return a_type
    
