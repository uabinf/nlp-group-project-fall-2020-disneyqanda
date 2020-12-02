# -*- coding: utf-8 -*-

import en_core_web_sm
nlp = en_core_web_sm.load()


def q_head_words(q):
    
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
