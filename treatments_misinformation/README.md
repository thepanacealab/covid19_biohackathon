# Characterize the information/misinformation around potential COVID-19 treatments using Twitter data
The objective of this project is to analyze whether Twitter data can be utilized to characterize the information related to treatments for COVID-19. For this project, we utilized our  [150+ million tweets of COVID-19 chatter](https://zenodo.org/record/3738018). The dataset consists of tweets from January 27th to April 6th, all related to COVID-19 chatter, for more details visit the pre-print for the dataset [150+ million tweets of COVID-19 chatter](https://arxiv.org/abs/2004.03688).

## Methodology
We annotated 150+ million tweets using the drug dictionary compiled from [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/index.html) with 19,643 drug terms. The drug dictionary generation process is explained in detail in our [paper](https://www.biorxiv.org/content/10.1101/859611v1). We utilized the NER tool from our [Social Media Mining Toolkit(SMMT)](https://arxiv.org/abs/2003.13894) for annotation. Since the language of Twitter is not structured, we implemented a spelling check module. We identified the top 200 drugs and generated misspellings for them. This spelling correction module consists of two parts
- Generate  misspellings for top 200 drugs - Generated using [Qmisspell](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6322919/) using [RedMed word embeddings](https://www.biorxiv.org/content/10.1101/663625v3.full). We generated 2,056 misspelled terms for the top 200 drug terms and added them to our vocabulary.
- Alter incorrect spellings of the tweet text before annotation - Implemented [Symspell](https://github.com/wolfgarbe/SymSpell) on the NER tagger

## Experiment Setup
We conducted 4 different experiments and the scenarios are listed here. All the experiments are performed on the 150+ million tweets dataset. 
- Annotate the tweet text using the drug term vocabulary generated from RxNorm and get counts.
- Add the spelling check module and alter the tweet text with the correct spellings and then generate the counts using drug term vocabulary. Covid-19 and related terms were added to the vocabulary which the spell checker uses.
- Annotate the tweet text with the misspelled terms added to the drug term vocabulary.
- Annotate the tweet text after spell check module with the misspelled terms added to the drug term vocabulary.


## Results
A total of **1,088,807** drug tweets were annotated using the drug dictionary prior to the spell check module. We identified **1,929** unique drug terms with 12,48,620 occurrences in 1,088,807 tweets. The following table consists of the top 10 identified drug terms.

| Drug Term     | No of Occurrences  | 
| ------------- | ------------- | 
| chloroquine  | 214036  |
|hydroxychloroquine|184607 |
|azithromycin|63642 |
|ibuprofen|60890 |
|agar|42069 |
|vicodin|25126 |
|plaquenil|23430 |
|advil|20739 |
|dettol|9188 |
|tylenol|5946 |
|cocaine|3955 |

The results for the remaining experiments will be updated soon. 

## Deliverables
The following tools and code are made available for reproducibility. 
- Annotation tool - **ner_en.py** - this utility will correct mispelled words in a tweet and then annotate tweets in a given TSV file when provided with a dictionary. Please look at our [SMMT NER](https://github.com/thepanacealab/SMMT/blob/master/data_annotationANDstandardization/README.md) documentation for usage
- Dictionaries - We provide two dictionaries. **panacea_sin.tsv** is the drug term dictionary compiled using RxNorm. **mispelled_terms.tsv** is the dictionary with 2,056 misspelled terms. The pid in misspelled term corresponds to the pid in the panacea_sin.tsv.
- Wordembedding model of Covid-19 chatter - This can be utilized in NLP research. (Will update soon)
- **Drug tweets** dataset in Covid-19 chatter - on request! 

## Things to do post hackathon
- Validate the results
- Analysis was perormed only on all the tweets which includes retweets. Perform the analysis for original tweets.
- Analysis was performed only on English language. Expand it to other languages. 
- Build ML models to automate.


