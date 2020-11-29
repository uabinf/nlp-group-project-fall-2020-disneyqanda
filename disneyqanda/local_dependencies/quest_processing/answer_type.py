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

# Figure out the correct NE type (person, place, or thing, etc)
# Look at question words in the question (regex)
# Question headwords (dependency parsers)
    
# Define a taxonomy of question types
# Annotate training data for each question type
# Train classifiers for each question class using a rich set of features
#import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()


def get_question_words(q_tokens):
    q_words = [x.lower() for x in q_tokens if x.lower() in ['who','what','how','when','where','which','why']]
    print("Question words found:",q_words,"\n")
    return q_words


def get_head_words(question):
    return ['height','requirement']


def get_head_words(q):
    doc = nlp(q)
    words = [(x.text, x.head.text, x.dep_) for x in doc]
    return words
    
    
    
def get_named_entities(q):
    doc = nlp(q)
    n_ents = [(x.text, x.label_) for x in doc.ents]
    print("Named entities found:", n_ents,"\n")
    return n_ents
    

def get_anstype_features(question):
    return {
        'question': question.q,
        'quest_words': get_question_words(question.q_tokens),
        'head_words': get_head_words(question.q),
        'entities': get_named_entities(question.q)        
            }
    
def q_answer_type(question):
     if question.q.find("height") > 0:
         a_type = "numeric, height"
     else:
         a_type = "not height"
         
     a_type = get_anstype_features(question)
     return a_type
 

