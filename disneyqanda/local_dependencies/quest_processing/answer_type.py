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
    
def q_answer_type(q):
     if q.q.find("height") > 0:
         a_type = "numeric, height"
     else:
         a_type = "not height"
     return a_type
    