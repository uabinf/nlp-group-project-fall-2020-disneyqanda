# -*- coding: utf-8 -*-

# Parse it into questions and answers
# Do any processing (tokenization, NER, etc)


def doc_segmentation(doc):
    
    seg = doc.split('.')
    print("Segmenting documents\n")
    return seg