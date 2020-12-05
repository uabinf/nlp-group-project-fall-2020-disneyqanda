# -*- coding: utf-8 -*-

# This file will handle all document processing
#   - Document retrieval
#   - Document segmentation
#   - Passage retrieval
#   - Passage ranking

from local_dependencies.doc_processing.document_retrieval import doc_retrieval
from local_dependencies.doc_processing.document_segmentation import doc_segmentation
from local_dependencies.doc_processing.passage_ranking import passage_ranking
    

def document_processing(question, key_words):
    print()
    print("_____________________________________________\nDocument Processing\n")
    
    doc_df = doc_retrieval()
    print(doc_df.size," documents retrieved\n")
    
    docs = doc_segmentation(doc_df, key_words)
    print(docs.size," passages retrieved\n")
       
    ranking = passage_ranking(question, docs)
    print("Passages ranked by cosine similarity:", ranking.head(10))
    
    return ranking

