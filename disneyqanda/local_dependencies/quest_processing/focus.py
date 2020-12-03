# -*- coding: utf-8 -*-

# Function to get head words, to find the focus of the question being asked

# import spaCy for dependency parsing
import en_core_web_sm
nlp = en_core_web_sm.load()


def q_head_words(q):
    
    # Use en_core_web_sm for dependency parsing
    doc = nlp(q)
    words = [(x.text, x.pos_, x.head.text, x.dep_) for x in doc]
    print("Dependency parsing:___________________________\n", words,"\n")
    
    # Get the root word
    root_word = [x[0] for x in words if x[3] == "ROOT"]
    print("Root word:", root_word,"\n")
    
    # Get words dependent on the root word
    dep_on_root = [x[0] for x in words if x[2] == root_word[0]]
    print("Words dependent on root:", dep_on_root,"\n")
    
    # Get nouns dependent on the root word
    nouns = [x[0] for x in words if x[1] == "NOUN" and x[0] in dep_on_root]
    print("Nouns dependent on root:", nouns,"\n")
    
    # Get adjectives describing it or nouns making it compound
    add_words = [x[0] for x in words if x[2] in nouns and x[3] in ["compound","ADJ"]]
    print("Words related to those nouns:", add_words, "\n")
    head_words = add_words + nouns
    print("Head words found:\n", head_words, "\n")
    return head_words
