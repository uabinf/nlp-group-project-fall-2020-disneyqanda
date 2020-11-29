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
import pandas as pd
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
    print("Dependency parsing:\n", words,"\n")
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
       # 'entities': get_named_entities(question.q)
            }
    
def q_answer_type(question):
     if question.q.find("height") > 0:
         a_type = "numeric, height"
     else:
         a_type = "not height"
         
     a_type = get_anstype_features(question)
     return a_type
 

def train_ans_type_model():
    # Read training data
    df_ans_type = pd.read_csv("data/Question_AnswerType.csv") 
    
    df_ans_type["features"] = df_ans_type["question"].apply(
            lambda x:get_anstype_features(Question(x))
            )
    
    train = []
    for index, row in df_ans_type.iterrows():
        train.append([row["features"],row["label"]])
    
    train    
    
    classifier = nltk.NaiveBayesClassifier.train(train)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

