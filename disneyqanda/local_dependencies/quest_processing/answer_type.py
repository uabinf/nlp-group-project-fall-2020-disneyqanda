# -*- coding: utf-8 -*-
        
# Define a taxonomy of question types
# Annotate training data for each question type
# Train classifiers for each question class using a rich set of features
#import spacy
from .key_words import q_key_words
from .focus import q_head_words

import pandas as pd
import pickle
import nltk
import en_core_web_sm
nlp = en_core_web_sm.load()


def get_question_words(q_tokens):
    q_words = [x.lower() for x in q_tokens if x.lower() in ['who','what','how','when','where','which','why','do','does','did','is']]
    print("Question words found:",q_words,"\n")
    return q_words

    
def get_named_entities(q):
    # Use en_core_web_sm to get named entities in the question
    doc = nlp(q)
    n_ents = [(x.text, x.label_) for x in doc.ents]
    print("Named entities found:", n_ents,"\n")
    return n_ents


def get_anstype_features(question):
    return {
        'question': question.q,
        'quest_words': ' '.join(get_question_words(question.q_tokens)),
        'head_words': ' '.join(q_head_words(question.q)),
        'entities': str(get_named_entities(question.q)).strip("[]")
            }
    
    
def q_answer_type(question):
    # Load the trained answer type classification model
    classifier_file = open("data/ans_type_classifier","rb")
    classifier_model = pickle.load(classifier_file)
    classifier_file.close()
    
    # Get the features for the question that was asked
    q_features = get_anstype_features(question)
    
    # Predict the answer type of the question
    a_type = classifier_model.classify(q_features)
    return a_type
 

# Run on-demand to train the model
def train_ans_type_model():
    # Read training data
    df_ans_type = pd.read_csv("data/Question_AnswerType.csv") 
    
    # Get the features for the training questions
    df_ans_type["features"] = df_ans_type["question"].apply(
            lambda x:get_anstype_features(Question(x))
            )
    
    # Declare an empty list to put the features and labels in
    train = []
    for index, row in df_ans_type.iterrows():
        train.append([row["features"],row["label"]])
    
    #train - Viewing data for sanity check    
    
    # Train classifier 
    classifier = nltk.NaiveBayesClassifier.train(train)
    
    # Save trained model
    save_classifier = open("data/ans_type_classifier","wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

