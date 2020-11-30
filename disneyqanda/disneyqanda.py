# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

from local_dependencies.disney_data import disney_entities
from local_dependencies.question import Question
from local_dependencies.document_processing import document_processing
from local_dependencies.answer_processing import answer_processing 

def main():
    
    # Load the Disney data
    df_disney_ent = pd.read_csv("data/DisneyEntities.csv")   
    df_disney = disney_entities(df_disney_ent)
    
    # Get the question
    #q = "Is there a height requirement for Star Wars: Rise of the Resistance?"
    # = "What is the height requirement for Star Wars: Rise of the Resistance?"
    q = "Which park is The Barnstormer in?"
    print("_____________________________________________\nQuestion:\n",q,"\n")
    
    # Instantiate the question object
    question = Question(q)
    print("Instantiating question object . . .\n")
    print("Question tokenized:\n", question.q_tokens,"\n")
    print("Question stopwords removed:\n", question.q_sw_removed,"\n")
    print("Question POS:\n", question.q_pos,"\n")
    print("_____________________________________________\nQuestion Processing\n")
    
            
    # Determine the question type
    q_type = question.question_type()
    print("Question Type:\n", q_type,"\n")
    
    # Find the query key words
    key_words = question.key_words(df_disney)
    print("Key Words Found:\n", key_words,"\n")
    
    # Get the question's focus
    focus = question.focus()
    print("Focus:\n", focus,"\n")
    
    # Get the question's relations
    rels = question.relations()
    print("Relations:\n", rels,"\n")
    
    # Determine the answer type
    ans_type = question.answer_type()
    print("Answer type:", ans_type,"\n")
    
    
    # Document Retrieval
    passage = document_processing(q)
    
    
    # Answer Processing
    a = answer_processing(question, passage)
    print("Answer:")
    print(a)
    
if __name__ == "__main__":
    main()      
