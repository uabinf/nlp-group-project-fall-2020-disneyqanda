# Disney Q & A
## UAB Fall 2020 CS 662 NLP 
The purpose of this project is to create a model that can answer questions about Disney World and Disney Land


## Authors

Deeptha Srirangam (MS Data Science student)

Leigh Allison (MS Data Science student)


![](images/Cover.PNG)

## Installation
```python
pip install git+https://github.com/uabinf/nlp-group-project-fall-2020-disneyqanda
```
## Usage
```python
import disneyqanda
```
## How it works
Ask a question about Disney World or Disney Land.
Disney Q & A has 4 main sections:
1) Data Retrieval
    * Use selenium to go to each webpage and BeautifulSoup to parse the data found in each webpage
    * Disney World
        * Go through 4 main categories: Walt Disney World Resort, Vacation Planning, MyMagic+, Website Support
        * Within the 4 main categories: go through subcategories which contain the list of questions
        * For each subcategory, get the list of questions with their answers
    * Disneyland
        * Go through 4 main categories: Disneyland Resort, Vacation Planning, Technical Support
        * Within the 4 main categories: go through subcategories which contain the list of questions
        * For each subcategory, get the list of questions with their answers
    * Create a textfile with the list of questions and answers in the following format:
        Q1
        A1
        Q2
        A2
        ....
2) Question Processing
    * Basic processing
        * Tokenize
        * Remove stopwords
        * POS tag
        * Remove punctuation
    * Get question words
    * Find key words 
        * Search against custom Disney entity list
        * Add adjective/noun pairs
    * Find focus
        * Dependency parsing
        * Get root word and words dependent on the root
        * Get nouns dependent on root and adjectives or nouns describing them
    * Determine answer type
        * nltk Naive Bayes model trained on lableed questions
        * Use features from question processing for the model
3) Document Processing
    * Document Retrieval
        * Read documents, join corresponding questions and answers
    * Document Segmentation
        * Given the list of documents from document retrieval, iterate through the questions and check to see if keywords from question processing appear in the question.
        * If there are keywords that match, add the answer to a list 
        * Returns a list of possible answers
    * Passage Retrieval 
        * Get the list of answers from Document Segmentation
    * Passage Ranking 
        * Doc2Vec model trained on all Disney questions and answers
        * Get embeddings of question being asked and questions mined from Disney
        * Use cosine similarity to get most similar questions
4) Answer Processing
    * NER tagger 
        * Search against custom Disney entity list
    * Candidate answers
        * Get questions with most matching words to question being asked
    * Ranking candidates
        * Check named entities in questions and answers
        * Check the answer type for each candidate answer's question
        * Choose the best match base on these features 

## Directory Structure
```bash
|-disneyqanda
|   |-disneyqanda.py (main file to run program)
|   |-data
|   |   |-ans_type_classifier (nltk Naive Bayes classification model)
|   |   |-doc2vec.model (gensim Doc2Vec model trained on qna.txt)
|   |   |-DisneyEntities.csv (custom Disney entity list)
|   |   |-qna.txt (Q and A data from Disney)
|   |   |-Question_AnswerType.csv (labeled data for training ans_type_classifier)
|   |-data_collection
|   |-local_dependencies
|   |   |-question.py (question object code)
|   |   |-document_processing.py (doc processing driver code)
|   |   |-answer_processing.py (answer processing driver code)
|   |   |-quest_processing
|   |   |   |-answer_type.py
|   |   |   |-focus.py 
|   |   |   |-key_words.py
|   |   |-doc_processing
|   |   |   |-document_retrieval.py
|   |   |   |-document_segmentation.py
|   |   |   |-passage_ranking.py
|   |   |   |-passage_retrieval.py
|   |   |-ans_processing
|   |   |   |-ner_tagger.py
|   |   |   |-candidate_answer.py
|   |   |   |-candidate_ranking.py
```

## Sample Runs
```
_____________________________________________
Question:
 How much does it cost to renew my annual pass? 

_____________________________________________
Question Processing

Question tokenized:
 ['How', 'much', 'does', 'it', 'cost', 'to', 'renew', 'my', 'annual', 'pass', '?'] 

Question stopwords removed:
 ['much', 'cost', 'renew', 'annual', 'pass', '?'] 

Key Words Found:
 ['much', 'cost', 'annual', 'pass'] 

Question words found: ['how', 'does'] 

Dependency parsing:___________________________
 [('How', 'ADV', 'much', 'advmod'), ('much', 'ADJ', 'cost', 'dobj'), ('does', 'AUX', 'cost', 'aux'), ('it', 'PRON', 'cost', 'nsubj'), ('cost', 'VERB', 'cost', 'ROOT'), ('to', 'PART', 'renew', 'aux'), ('renew', 'VERB', 'cost', 'xcomp'), ('my', 'DET', 'pass', 'poss'), ('annual', 'ADJ', 'pass', 'amod'), ('pass', 'NOUN', 'renew', 'dobj'), ('?', 'PUNCT', 'cost', 'punct')] 

Root word: ['cost'] 

Words dependent on root: ['much', 'does', 'it', 'cost', 'renew', '?'] 

Nouns dependent on root: [] 

Words related to those nouns: [] 

Head words found:
 ['cost'] 

Named entities found: [('annual', 'DATE')] 

Answer type: cost 


_____________________________________________
Document Processing

1976  documents retrieved

468  passages retrieved

Ranking passages

Passages ranked by cosine similarity:                                             question  ...     score
0     How much does it cost to renew my annual pass?  ...  0.926245
1  I am a Florida resident. Can I renew my Annual...  ...  0.638627
2  Can I renew an Annual Pass for a Guest other t...  ...  0.747848
3  I didn't receive my renewal notice and need to...  ...  0.883498
4  Why am I getting an error message when I try t...  ...  0.704330
5  If I purchase a select Florida Resident Annual...  ...  0.991983
6  What proof of residence will I need to provide...  ...  1.224057
7  I’m an Annual Passholder. How often will I rec...  ...  0.694114
8  Do Annual Passholders receive discounts on the...  ...  0.863522
9        How much does it cost to park at the parks?  ...  0.632522

[10 rows x 6 columns]

Answer Processing
Running NER tagger on passages

Selecting candidate answers

Ranking candidate answers

Cosine score: [1.0090003]
Word matches: [5]
Answer's answer type: ['cost']
Best answer:
 ['You can view Passholder status renewal prices online, , ask at any Walt Disney World ticket window and call (407) 560-PASS or (407) 560-7277. Guests under 18 years of age must have parent or guardian permission to call.There are 3 convenient ways to renew your Passholder status:Renew online, Renew at any Walt Disney World Resort theme park ticket window or Disney Springs Guest Relations location.Renew over the phone by calling (407) 560-PASS or (407) 560-7277. Guests under 18 years of age must have parent or guardian permission to call.If you are renewing through the Monthly Payment Program for Florida residents, phone renewals are not available. However, you can renew online, in person at a theme park ticket window or Guest Relations location.Though the pass owner does not need to be present for renewal, each Annual Passholder will need to be present at the ticket window to receive his or her pass.If you purchased your current pass before October 4, 2015, you may be asked to select one of the new pass types available at the time of your renewal.Learn more about Annual Passes,  or purchase a new Annual Pass.']
 ```
