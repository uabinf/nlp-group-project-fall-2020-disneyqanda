# -*- coding: utf-8 -*-

# Function to get head words, to find the focus of the question being asked

# import spaCy for dependency parsing
import en_core_web_sm
nlp = en_core_web_sm.load()


def a_head_words(a):
    
    # Use en_core_web_sm for dependency parsing
    doc = nlp(a)
    words = [(x.text, x.pos_, x.head.text, x.dep_) for x in doc]
    
    # Get the root word
    root_word = [x[0] for x in words if x[3] == "ROOT"]
    
    # Get words dependent on the root word
    dep_on_root = [x[0] for x in words if x[2] == root_word[0]]
    
    # Get nouns dependent on the root word
    nouns = [x[0] for x in words if x[1] == "NOUN" and x[0] in dep_on_root]
    
    # Get adjectives describing it or nouns making it compound
    add_words = [x[0] for x in words if x[2] in nouns and x[3] in ["compound","ADJ"]]
    head_words = add_words + nouns
    return head_words
