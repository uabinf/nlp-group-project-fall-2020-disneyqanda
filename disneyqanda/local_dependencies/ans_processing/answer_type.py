# -*- coding: utf-8 -*-
        
# Define a taxonomy of question types
# Annotate training data for each question type
# Train a classifier for question using a rich set of features
#import spacy
from .key_words import a_key_words
from .focus import a_head_words

import pandas as pd
import pickle
import nltk
import en_core_web_sm
nlp = en_core_web_sm.load()


def get_question_words(a_tokens):
    a_words = [x.lower() for x in a_tokens if x.lower() in ['who','what','how','when','where','which','why','do','does','did','is']]
    return a_words

    
def get_named_entities(a):
    # Use en_core_web_sm to get named entities in the question
    doc = nlp(a)
    n_ents = [(x.text, x.label_) for x in doc.ents]
    return n_ents


def get_anstype_features(answer, keys):
    return {
        'a_question': answer.a,
        'quest_words': ' '.join(get_question_words(answer.a_tokens)),
        'head_words': ' '.join(a_head_words(answer.a)),
        'key_words': ''.join(keys),
        'entities': str(get_named_entities(answer.a)).strip("[]")
            }
    
    
def a_answer_type(answer, keys):
    # Load the trained answer type classification model
    classifier_file = open("data/ans_type_classifier","rb")
    classifier_model = pickle.load(classifier_file)
    classifier_file.close()
    
    # Get the features for the question that was asked
    a_features = get_anstype_features(answer, keys)
    
    # Predict the answer type of the question
    a_type = classifier_model.classify(a_features)
    return a_type
 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

