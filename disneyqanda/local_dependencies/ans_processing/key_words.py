# -*- coding: utf-8 -*-

# Function to find the key words in the question being asked


def a_key_words(answer, df_disney):
    key_words = []
    
    ## Get nouns with adjective modiers
    # Add them to the key words list
    for index in range(len(answer.a_pos)-1):
        if (answer.a_pos[index][1] == 'ADJ') & (answer.a_pos[index+1][1] == 'NOUN'):
            key_words.append(answer.a_pos[index][0])
            key_words.append(answer.a_pos[index+1][0]) 
            
    
    ## Get any words in our Disney entity list
    # Get the # of words in each Disney entity
    df_disney["total"] = df_disney["tokens_sw_removed"].apply(lambda x: len(x))
    
    # Get the words from the question that are in each Disney entity
    df_disney["winq"] = df_disney["tokens_sw_removed"].apply(
            lambda x: [w for w in x if w in answer.a_no_punc]
            )
    
    # Get the number of words that were found for each entity
    df_disney["winq_len"] = df_disney["winq"].apply(lambda x: len(x))
    
    # Get the ratio between words found in each entity and words in each entity
    df_disney["match"] = df_disney["winq_len"]/df_disney["total"]
    
    # Get the words from the question with the highest ratio of matching an entity
    # Add them to the key words list
    key_words.extend(df_disney["winq"][df_disney["match"] == df_disney["match"].max()].iloc[0])
            
    
    return key_words