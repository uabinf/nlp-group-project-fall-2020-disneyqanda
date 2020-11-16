# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from local_dependencies.question import Question
from local_dependencies.document_processing import document_processing
from local_dependencies.answer_processing import answer_processing 

def main():
    
    # Get the question
    q = "Is there a height requirement for Star Wars: Rise of the Resistance?"
    print("Question:")
    print(q)
    
    # Instantiate the question object
    question = Question(q)
    print()
    print("Start Question Processing")
            
    # Determine the question type
    q_type = question.question_type()
    print("question type:", q_type)
    
    # Find the query key words
    key_words = question.key_words()
    print("key words:", key_words)
    
    # Get the question's focus
    focus = question.focus()
    print("focus:", focus)
    
    # Get the question's relations
    rels = question.relations()
    print("relations:", rels)
    
    # Determine the answer type
    ans_type = question.answer_type()
    print("answer type:", ans_type)
    
    # Document Retrieval
    passage = document_processing(q)
    
    
    # Answer Processing
    a = answer_processing(question, passage)
    print()
    print("Answer:")
    print(a)
    
    
main()    
