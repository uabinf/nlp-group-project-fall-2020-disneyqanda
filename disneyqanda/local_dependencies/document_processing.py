# -*- coding: utf-8 -*-

# This file will handle all document processing
#   - Document retrieval
#   - Document segmentation
#   - Passage retrieval
#   - Passage ranking

#from local_dependencies.doc_processing.document_retrieval import doc_retrieval
from local_dependencies.doc_processing.document_segmentation import doc_segmentation
from local_dependencies.doc_processing.passage_ranking import passage_ranking
    

def document_processing(q, key_words):
    print()
    print("_____________________________________________\nDocument Processing\n")
    #doc = doc_retrieval()
    
    seg = doc_segmentation(key_words)
       
    ranking = passage_ranking(seg)
    print("Rank:", ranking)
    
    return passage

