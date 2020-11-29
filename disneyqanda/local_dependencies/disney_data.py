# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

 
def disney_entities(df_disney):
    stop_words = set(stopwords.words('english'))

    df_disney["tokens"] = df_disney["Entity"].apply(lambda x: word_tokenize(x))
    df_disney["tokens_sw_removed"] = df_disney["tokens"].apply(
            lambda x: [w.lower() for w in x if not w.lower() in stop_words]
            )
   
    return df_disney