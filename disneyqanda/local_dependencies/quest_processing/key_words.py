# -*- coding: utf-8 -*-

# Select non-stopwords in quotatations
# Select recognized named entities
# Select Complex nominals with their adjectival modifiers
# Select all other complex nominals
# Select all nouns with their adjectival modifiers
# Select all other nouns
# Select all verbs
# Select all adverbs
# Select the QFW word (skipped in all previous steps)
# Select all other words
    

def q_key_words(question, df_disney):
    key_words = []
    
    ## Get nouns with adjective modiers
    question.q_pos[0][1]
    for index in range(len(question.q_pos)-1):
        if (question.q_pos[index][1] == 'ADJ') & (question.q_pos[index+1][1] == 'NOUN'):
            key_words.append(question.q_pos[index][0])
            key_words.append(question.q_pos[index+1][0]) 
            
    
    ## Get any words in our Disney entity list
    # Get the # of words in each Disney entity
    df_disney["total"] = df_disney["tokens_sw_removed"].apply(lambda x: len(x))
    
    # Get the words from the question that are in each Disney entity
    df_disney["winq"] = df_disney["tokens_sw_removed"].apply(
            lambda x: [w for w in x if w in question.q_no_punc]
            )
    
    # Get the number of words that were found for each entity
    df_disney["winq_len"] = df_disney["winq"].apply(lambda x: len(x))
    
    # Get the ratio between words found in each entity and words in each entity
    df_disney["match"] = df_disney["winq_len"]/df_disney["total"]
    
    # Get the words from the question with the highest ratio of matching an entity
    key_words.extend(df_disney["winq"][df_disney["match"] == df_disney["match"].max()].iloc[0])
            
    
    return key_words