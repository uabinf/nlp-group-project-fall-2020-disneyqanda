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
    q = "Is there a height requirement for Star Wars: Rise of the Resistance?"
    print("Question:")
    print(q)
    
    # Instantiate the question object
    question = Question(q)
    print("Question Processing\n")
    print("Question tokenized:", question.q_tokens,"\n")
    print("Question stopwords removed:", question.q_sw_removed,"\n")
    print("Question POS:", question.q_pos,"\n")
            
    # Determine the question type
    q_type = question.question_type()
    print("question type:", q_type,"\n")
    
    # Find the query key words
    key_words = question.key_words(df_disney)
    print("key words:", key_words,"\n")
    
    # Get the question's focus
    focus = question.focus()
    print("focus:", focus,"\n")
    
    # Get the question's relations
    rels = question.relations()
    print("relations:", rels,"\n")
    
    # Determine the answer type
    ans_type = question.answer_type()
    print("answer type:", ans_type,"\n")
    
    
    # Document Retrieval
    passage = document_processing(q)
    
    
    # Answer Processing
    a = answer_processing(question, passage)
    print("Answer:")
    print(a)
    
if __name__ == "__main__":
    main()      
