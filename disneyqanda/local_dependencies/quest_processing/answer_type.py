# -*- coding: utf-8 -*-
        
# Define a taxonomy of question types
# Annotate training data for each question type
# Train classifiers for each question class using a rich set of features
#import spacy
import pandas as pd
import pickle
import nltk
import en_core_web_sm
nlp = en_core_web_sm.load()


def get_question_words(q_tokens):
    q_words = [x.lower() for x in q_tokens if x.lower() in ['who','what','how','when','where','which','why','do','does','did','is']]
    print("Question words found:",q_words,"\n")
    return q_words


def get_head_words(q):
    # Use en_core_web_sm for dependency parsing
    doc = nlp(q)
    words = [(x.text, x.pos_, x.head.text, x.dep_) for x in doc]
    print("Dependency parsing:___________________________\n", words,"\n")
    root_word = [x[0] for x in words if x[3] == "ROOT"]
    print("Root word:", root_word,"\n")
    dep_on_root = [x[0] for x in words if x[2] == root_word[0]]
    print("Words dependent on root:", dep_on_root,"\n")
    nouns = [x[0] for x in words if x[1] == "NOUN" and x[0] in dep_on_root]
    print("Nouns dependent on root:", nouns,"\n")
    add_words = [x[0] for x in words if x[2] in nouns and x[3] == "compound"]
    print("Words related to those nouns:", add_words, "\n")
    head_words = add_words + nouns
    print("Head words found:\n", head_words, "\n")
    return head_words
    
    
def get_named_entities(q):
    # Use en_core_web_sm to get named entities in question
    doc = nlp(q)
    n_ents = [(x.text, x.label_) for x in doc.ents]
    print("Named entities found:", n_ents,"\n")
    return n_ents
    

def get_anstype_features(question):
    return {
        'question': question.q,
        'quest_words': ' '.join(get_question_words(question.q_tokens)),
        'head_words': ' '.join(get_head_words(question.q)),
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

