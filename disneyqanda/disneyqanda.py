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
    
    # Load the Disney entity list
    df_disney_ent = pd.read_csv("data/DisneyEntities.csv")   
    df_disney = disney_entities(df_disney_ent)
        
    # Get the question
    #q = "Is there a height requirement for Star Wars: Rise of the Resistance?"
    q = "What kinds of prices can I expect to pay for food inside the theme parks and at Disney Resort hotels?"
    
    print("_____________________________________________\nQuestion:\n",q,"\n")
    
    # Instantiate the question object
    question = Question(q)
    print("_____________________________________________\nQuestion Processing\n")
    print("Question tokenized:\n", question.q_tokens,"\n")
    print("Question stopwords removed:\n", question.q_sw_removed,"\n")
    #print("Question POS:\n", question.q_pos,"\n")
    
            
    # Find the query key words
    key_words = question.key_words(df_disney)
    print("Key Words Found:\n", key_words,"\n")
    
    
    # Determine the answer type
    ans_type = question.answer_type(key_words)
    print("Answer type:", ans_type,"\n")
    
    
    # Document Retrieval
    ranking = document_processing(question, key_words)
    
    
    # Answer Processing
    answer = answer_processing(question, ranking, df_disney, ans_type)
    print("Best answer:\n", str(answer.answer.values))
    
    
if __name__ == "__main__":
    main()      
