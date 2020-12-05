# -*- coding: utf-8 -*-

# Run an answer type ner tagger on the passages
# Can be full ner, simple regex, or hybrid

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

from local_dependencies.disney_data import disney_entities


def ner_tagger(ranking):
    print("Running NER tagger on passages\n")
    
    # Add an empty field for the entities found
    ranking['entity'] = ""
    
    # Load the Disney entity list
    df_disney_ent = pd.read_csv("data/DisneyEntities.csv")   
    df_disney_a = disney_entities(df_disney_ent)
    # POS tag them
    df_disney_a['tokens_pos'] = df_disney_a['tokens_sw_removed'].apply(
            lambda x: nltk.pos_tag(x, tagset='universal')
            )
    # Remove punctuation
    df_disney_a['no_punc'] = df_disney_a['tokens_pos'].apply(
            lambda x: [w[0] for w in x if not w[1] == "."]
            )
    # Remove noun-marked apostrophes
    df_disney_a['no_punc'] = df_disney_a['no_punc'].apply(
            lambda x: [w for w in x if not ((w == "’") or (w == "‘"))]
            )
   # Get the # of words in each Disney entity
    df_disney_a["total"] = df_disney_a["no_punc"].apply(lambda x: len(x))

    
    
    for index, row in ranking.iterrows():
        #print(row['tokens'])
        
        # Get the words from each question/answer that are in each Disney entity
        df_disney_a["winq"] = df_disney_a["no_punc"].apply(
                lambda x: [w for w in x if w in row['no_punc']]
                )
    
        # Get the number of words that were found for each entity
        df_disney_a["winq_len"] = df_disney_a["winq"].apply(lambda x: len(x))
    
        # Get the ratio between words found in each entity and words in each entity
        df_disney_a["match"] = df_disney_a["winq_len"]/df_disney_a["total"]
    
        # Get the words from the question with the highest ratio of matching an entity
        words = []
        words = (df_disney_a["no_punc"][df_disney_a["match"] == df_disney_a["match"].max()].iloc[0])
        ranking.loc[index, 'entity'] = ' '.join(words)
        
        
    return ranking
    