# -*- coding: utf-8 -*-

# Rule-based classifiers or supervised ML

# Features for passage ranking:
#   - Number of named entities of the right type in passage
#   - Number of query words in passage
#   - Number of question N-grams in passage
#   - Longest sequence of question words
#   - Rank of the document containing passage

def passage_ranking(psg):
    rank = 1
    print("Ranking passages\n")
    return rank