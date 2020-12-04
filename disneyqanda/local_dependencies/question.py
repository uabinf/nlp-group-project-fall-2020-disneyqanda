# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:08:25 2020

Question Class

Initialization tokenizes, removes stopwords, pos tags, and removes punctuation.
Answer type function gets the other question features.
    
"""
from local_dependencies.quest_processing.answer_type import q_answer_type
from local_dependencies.quest_processing.key_words import q_key_words

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))


class Question:
    def __init__(self, q):
        self.q = q
        # Tokenize the question
        self.q_tokens = word_tokenize(q)
        # Remove stopwords
        self.q_sw_removed = [w.lower() for w in self.q_tokens if not w.lower() in stop_words]
        # POS tag it
        self.q_pos = nltk.pos_tag(self.q_sw_removed, tagset='universal')
        # Remove punctuation
        self.q_no_punc = [w[0] for w in self.q_pos if not w[1] == "."]
            
        
    # Get the query key words
    def key_words(self, entities):
        keys = q_key_words(self, entities)
        return keys
        
     
    # Determine the answer type 
    def answer_type(self, keys):
        q_a_type = q_answer_type(self)
        return q_a_type
    
    
    
    