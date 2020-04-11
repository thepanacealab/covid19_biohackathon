#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   /$$$$$$  /$$      /$$ /$$      /$$ /$$$$$$$$
#  /$$__  $$| $$$    /$$$| $$$    /$$$|__  $$__/
# | $$  \__/| $$$$  /$$$$| $$$$  /$$$$   | $$   
# |  $$$$$$ | $$ $$/$$ $$| $$ $$/$$ $$   | $$   
#  \____  $$| $$  $$$| $$| $$  $$$| $$   | $$   
#  /$$  \ $$| $$\  $ | $$| $$\  $ | $$   | $$   
# |  $$$$$$/| $$ \/  | $$| $$ \/  | $$   | $$   
#  \______/ |__/     |__/|__/     |__/   |__/  
#
#
# Developed during Biomedical Hackathon 6 - http://blah6.linkedannotation.org/
# Authors: Ramya Tekumalla, Javad Asl, Juan M. Banda
# Contributors: Kevin B. Cohen, Joanthan Lucero

from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import csv
import spacy
import glob
import os
import argparse
import pickle
import json
from itertools import islice
import pkg_resources
from symspellpy import SymSpell
import argparse
import pandas as pd

sym_spell = SymSpell()
drug_dict_path = "counts_alltweets.tsv"
eng_dict_path = "dict/en-80k.txt"

def tagged_docs(docs,name):
	counter = 0.0
	keys = set()
	for key in docs:
		if len(docs[key].ents) > 0:
			keys.add(key)
			counter = counter + 1
	print(name, counter,len(docs),counter/len(docs))
	return keys

parser = argparse.ArgumentParser()
   
parser.add_argument('-d', help="Dictionary file with extension", required=True)
parser.add_argument('-i',  help="Input file name with extension", required=True)
parser.add_argument('-o',  help="Output file name with extension", required=True)
parser.add_argument('-c',  help="Output file name with extension", required=True)



args = parser.parse_args()
dictionary_filename = args.d
input_file = args.i
output_file = args.o
drugcount_file = args.c

temp = open(dictionary_filename)
dictionary_file = csv.reader(temp, delimiter='\t')
patterns = []
i = 0
for product in dictionary_file:
	if i ==0:
		i = i +1
		continue
	patterns.append({"label":product[1],"pattern":product[2]})

temp.close()
#print(len(patterns))

nlp = English()
ruler = EntityRuler(nlp)

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
drugCount = {}
fL = open(drugcount_file, 'w')
fO = open(output_file,"w",encoding="utf-8")
fC = open("corrected_tweets.txt", "w")

data = pd.read_csv(input_file, sep='\t',encoding = 'utf8',lineterminator='\n', usecols = [0,3,6], names=['id_str','full_text','lang'] ,low_memory=False, dtype=str)
data["id_str"]=data["id_str"].astype(str)
data["full_text"]=data["full_text"].astype(str)
data["lang"] = data["lang"].astype(str)
data['id_str'].dropna(inplace=True)


for index, row in data.iterrows():
    tweetId = row['id_str']
    tweetText = row['full_text'].lower()
    language = row['lang'].lower()
    if language=="en":
        suggestions = sym_spell.lookup_compound(tweetText, max_edit_distance=2)
        corrected_TweetText = " ".join(str(suggestion._term) for suggestion in suggestions)
        #print(corrected_TweetText)                       
        desc = nlp(corrected_TweetText)
        #print(tweetText)
        #print(desc.ents)
        if(len(desc.ents))>0:
            tweetText = tweetText.replace("\r","")
            tweetText = tweetText.replace("\n","")
            fO.write(str(tweetId) + "\t" + str(tweetText) + "\n")
            fC.write(str(tweetId) + "\t" + str(corrected_TweetText) + "\n")

            
        for item in desc.ents:
            if str(item) in drugCount:
                drugCount [str(item)]+=1
            else:
                drugCount [str(item)]=1 

sorted_by_value = sorted(drugCount.items(), key=lambda kv: kv[1], reverse = True)
for i in sorted_by_value:
    fL.write(i[0] + "\t" + str(i[1]) + "\n")
#Dkeys = tagged_docs(extended_docs,'description')
#print(len(Dkeys))

fO.close()