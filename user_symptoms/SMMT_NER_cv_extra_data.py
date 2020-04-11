from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import csv
import spacy
import glob
import os
import argparse
import pickle
import json
import pandas as pd

def tagged_docs(docs,name):
	counter = 0.0
	keys = set()
	for key in docs:
		if len(docs[key].ents) > 0:
			keys.add(key)
			counter = counter + 1
	print(name, counter,len(docs),counter/len(docs))
	return keys

def genericFormat(ID,description,desc,i,csv_output):
	if i ==0:
		csv_output.writerow(['DocumentID', 'TermID', 'SpanStart','SpanEnd'])
	if len(desc.ents) > 0:
		for ent in desc.ents:
			csv_output.writerow([ID,ent.label_, ent.start_char, ent.end_char])

def bratFormat(description,desc,fO,i):
	#print(len(desc.ents))
	if len(desc.ents) > 0:
		for ent in desc.ents:
			fO.write("T" + str(i) + "\t" + str(ent.label_) + "\t" + str(ent.start_char) + "\t" + str(ent.end_char) + "\t" + str(ent.text) + "\n")


def textAnFormat(description,desc,fO):
		text = "text"
		obj = "DrugTerm"
		deno = "denotations"
		span = "span"
		begin = "begin"
		end = "end"

		fO.write('{ "' + text + '":' + json.dumps(description) + " , \"" + deno + "\": [ ")
		count = 0
		if len(desc.ents) > 0:
			for ent in desc.ents:
				fO.write('{ "' + span + '"' + ":{" + '"' + begin + '"' + ":" + str(ent.start_char) + "," +  '"' + end +  '"' + ":" + str(ent.end_char) + "}" + "," + '"' + "obj" + '"' + ":" + '"' + obj + '"' + " }")  #+ ":" + '"{}"'.format(description) , ent.start_char, ent.end_char
				count += 1
				if count != len(desc.ents):
					fO.write(",")
			fO.write("] }" + "\n")

parser = argparse.ArgumentParser()
   
parser.add_argument('-d', help="Dictionary file with extension", required=True)
parser.add_argument('-i',  help="Input file name with extension", required=True)
parser.add_argument('-o',  help="Output file name with extension", required=True)
parser.add_argument('-f',  help="format f the annotation", default = "g")


args = parser.parse_args()
dictionary_filename = args.d
input_file = args.i
output_file = args.o
format_given = args.f
#print(format_given)

temp = open(dictionary_filename)
dictionary_file = csv.reader(temp, delimiter='\t')
patterns = []
i = 0
for product in dictionary_file:
	if i ==0:
		i = i +1
		continue
	patterns.append({"label":product[0],"pattern":product[1]})

temp.close()
#print(len(patterns))

nlp = English()
ruler = EntityRuler(nlp)

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
##### Open document
#products_raw = open(input_file)
#products = csv.reader(products_raw,delimiter='\t')

data = pd.read_csv(input_file, sep='\t',encoding = 'utf8',lineterminator='\n', usecols = [0,3], names=['id_str','text'] ,low_memory=False, dtype=str, skiprows=1)
data["id_str"]=data["id_str"].astype(str)
data["text"]=data["text"].astype(str)
data['id_str'].dropna(inplace=True)

extended_docs={}

if (format_given is "g"):
	f_output = open(output_file, 'w', newline='')
	csv_output = csv.writer(f_output, delimiter='\t')
if (format_given is "t" or "b" or "c"):
	fO = open(output_file, "w", encoding="utf-8")
i = 1

for index, row in data.iterrows():
	ID = row['id_str']
	description = row['text'].lower()

	if (format_given is "g"):
		desc = nlp(description)
		extended_docs[ID] = desc	
		genericFormat(ID,description,desc,i,csv_output)

	if (format_given is "b"):
		desc = nlp(description)
		extended_docs[ID] = desc	
		bratFormat(description,desc,fO,i)


	if (format_given is "t"):
		desc = nlp(description)
		textAnFormat(description, desc, fO)

	i = i+1


#products_raw.close()

#Dkeys = tagged_docs(extended_docs,'description')
#print(len(Dkeys))

del extended_docs
if (format_given is "t" or "b"):
	fO.close()
else:
	f_output.close()
