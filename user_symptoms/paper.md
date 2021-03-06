---
title: 'Identification and attribution of COVID-19 symptoms using Twitter data'
tags:
  - social media analysis
  - text mining
authors:
  - name: Juan M. Banda
    orcid: 0000-0001-8499-824X
    affiliation: 1
  - name: Ramya Tekumalla
    orcid: 0000-0002-1606-4856
    affiliation: 1
affiliations:
 - name: Georgia State University, 25 Park Place, Atlanta, USA
   index: 1
date: 11 April 2020
bibliography: paper.bib
---

# Introduction or Background

In this project we decided to use our dataset of [150+ million tweets of COVID-19 chatter](https://zenodo.org/record/3738018) to see if we could identify users mentioning COVID-19 related symptoms. The dataset consists of tweets from January 27th to April 6th, all related to COVID-19 chatter, for more details visit the pre-print for the dataset [here](https://arxiv.org/abs/2004.03688). 

## Methodology

After filtering for retweets, bots, and suspicious accounts (the ones that tweet several hundred times a day), we annotated and analized 30,990,645 tweets. Our annotation process was performed with the NER annotator from the [Social Media Mining Toolkit (SMMT)](https://arxiv.org/abs/2003.13894). Our first step was to use a dictionary comprised of terms from SNOMED, MeSH, ICD9/10, CPT, etc. extracted from the OHDSI vocabulary. Note that we included the latest version of this vocabulary includes COVID-19 terms. With this dictionary of 4 million unique terms we produced over 308 million annotations on the filtered set of tweets.

In order to narrow down the symptoms and additional COVID-19 clinical observations we used lists of prevalent COVID-19 related terms extracted from EHR's and made publicly available by the [Shah lab of Stanford](https://medium.com/@nigam/an-ehr-derived-summary-of-the-presenting-symptoms-of-patients-screened-for-sars-cov-2-910ceb1b22b9) with additions released by the Mayo clinic on their [MedTagger software](https://github.com/OHNLP/MedTagger/tree/master/src/main/resources/medtaggerieresources/covid19).

## Results

Focusing on these 50+ terms, without adding misspellings we identified a total of 435,482 annotations on 347,993 unique Tweets. Here is the list of top 10:

| Term          | Frequency |
| ------------- | --------- |
|pneumonia      |	110124    |
|infection      |	71882     |
|influenza      | 36390     |
|cough          |	35753     |
|anxiety        | 34658     |
|pain           | 12773     |
|depression     |	12189     |
|asthma         | 8307      |
|oxygen         | 5511      |
|ibuprofen      | 5310      |

So we made it to find 264,132 unique Twitter users that discussed the preselected symptoms and clinical observations. So we now how to disambiguate their claims.

However, this is not including misspellings, which are very prevalent in Twitter. So we took the 50+ common symptoms and clinical finding and generated their common misspellings
based on traditional lists of common misspellings and keyboard layout. Producing an additional dictionary of around 5,400 terms.

With these annotations, we were able to find that these are the top 10 most mispelled words:

| Term          | Frequency |
| ------------- | --------- |
| pneumonia     |	134242    |
| rash          |	130023    |
| infection     |	122544    |
| rales         |	53330     |
| influenza     |	47215     |
| anxiety       |	45520     |
| pain          |	29918     |
| depression    | 15021     |
| asthma        | 11399     |
| ibuprofen     | 8419      |

These allowed us to find an extra 653,431 annotations from 525,392 relevant unique tweets. These tweets come from an additional 176,121 unique Twitter users.

Overall, we recovered  873,385 relevant Tweets (for this subset of 50+ terms) leading us to 440,253 unique users we need to further evaluate to ascertain their claims.

## What are we releasing as a deliverable for this biohackathon - found in this repository
* Annotation code
* Dictionary files (OHDSI dictionary, symptoms dictionary, and mispellings dictionary)
* Tweet annotations - Upon Request
* Note: All manipulations and counts of the annotations were done using SQL on a PostgreSQL database. Scripts and queries will be added later.

## Things to do post hackathon
* Collect additional data for the identified users. 
* Perform small manual review/annotation.
* Build ML models to automate. 
* Expand EHR term list from findings on Twitter.

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

# Acknowledgements
Please always remember to acknowledge the BioHackathon, CodeFest, VoCamp, Sprint or similar where this work was (partially) developed.

# References

Leave thise section blank, create a paper.bib with all your references.
