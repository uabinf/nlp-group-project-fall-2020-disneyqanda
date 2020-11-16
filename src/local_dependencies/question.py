# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:08:25 2020

Question Class

"""
from local_dependencies.quest_processing.answer_type import q_answer_type
from local_dependencies.quest_processing.question_type import q_question_type
from local_dependencies.quest_processing.key_words import q_key_words
from local_dependencies.quest_processing.focus import q_focus
from local_dependencies.quest_processing.relations import q_relations

class Question:
    def __init__(self, q):
        self.q = q
    
    
     # Question type classification
    def question_type(self):
        q_type = q_question_type(self)
        return q_type
    
    
    # Get the query key words
    def key_words(self):
        keys = q_key_words(self)
        return keys
    
    
    # Focus detection
    def focus(self):
        foc = q_focus(self)
        return foc
    
    
    # Relation extraction
    def relations(self):
        rels = q_relations(self)
        return rels
        

    # Determine the answer type 
    def answer_type(self):
        q_a_type = q_answer_type(self)
        return q_a_type
    
    