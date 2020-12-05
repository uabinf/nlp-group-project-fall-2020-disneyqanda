"""
Answer Class

Initialization tokenizes, removes stopwords, pos tags, and removes punctuation.
Answer type function gets the other question features.
    
"""
from local_dependencies.ans_processing.answer_type import a_answer_type
from local_dependencies.ans_processing.key_words import a_key_words

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))


class Answer:
    def __init__(self, a):
        self.a = a
        # Tokenize the question
        self.a_tokens = word_tokenize(a)
        # Remove stopwords
        self.a_sw_removed = [w.lower() for w in self.a_tokens if not w.lower() in stop_words]
        # POS tag it
        self.a_pos = nltk.pos_tag(self.a_sw_removed, tagset='universal')
        # Remove punctuation
        self.a_no_punc = [w[0] for w in self.a_pos if not w[1] == "."]
            
        
    # Get the query key words
    def key_words(self, entities):
        keys = a_key_words(self, entities)
        return keys
        
     
    # Determine the answer type 
    def answer_type(self, keys):
        a_a_type = a_answer_type(self, keys)
        return a_a_type
    
    
    
    