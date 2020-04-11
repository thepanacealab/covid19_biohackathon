import pandas as pd
from random import randint
import sys
import random

def butterfinger(text,keyboard='querty'):

	keyApprox = {}
	typos = []
	if keyboard == "querty":
		keyApprox['q'] = "qwasedzx"
		keyApprox['w'] = "wqesadrfcx"
		keyApprox['e'] = "ewrsfdqazxcvgt"
		keyApprox['r'] = "retdgfwsxcvgt"
		keyApprox['t'] = "tryfhgedcvbnju"
		keyApprox['y'] = "ytugjhrfvbnji"
		keyApprox['u'] = "uyihkjtgbnmlo"
		keyApprox['i'] = "iuojlkyhnmlp"
		keyApprox['o'] = "oipklujm"
		keyApprox['p'] = "plo['ik"

		keyApprox['a'] = "aqszwxwdce"
		keyApprox['s'] = "swxadrfv"
		keyApprox['d'] = "decsfaqgbv"
		keyApprox['f'] = "fdgrvwsxyhn"
		keyApprox['g'] = "gtbfhedcyjn"
		keyApprox['h'] = "hyngjfrvkim"
		keyApprox['j'] = "jhknugtblom"
		keyApprox['k'] = "kjlinyhn"
		keyApprox['l'] = "lokmpujn"

		keyApprox['z'] = "zaxsvde"
		keyApprox['x'] = "xzcsdbvfrewq"
		keyApprox['c'] = "cxvdfzswergb"
		keyApprox['v'] = "vcfbgxdertyn"
		keyApprox['b'] = "bvnghcftyun"
		keyApprox['n'] = "nbmhjvgtuik"
		keyApprox['m'] = "mnkjloik"
		keyApprox[' '] = " "
	else:
		print ("Keyboard not supported.")

	words = text.split()
	nwords = len(words)
	bb=0
	for word in words:
		tempW = word
		for a in range(len(tempW)): 
			temp = keyApprox[tempW[a]]
			for b in range(len(temp)):
				fixed = tempW[:a] + temp[b] + tempW[a + 1:] 
				if nwords==1:
					typos.append(fixed)
				elif (nwords==2 and bb ==0):
					typos.append(fixed + " " + words[1])
				elif (nwords==2 and bb ==1):
					typos.append(words[0] + " " + fixed)
				elif (nwords==3 and bb==0):
					typos.append(fixed + " " + words[1] + " " + words[2])
				elif (nwords==3 and bb==1):
					typos.append(words[0] + " " + fixed + " " + words[2])
				elif (nwords==3 and bb==2):
					typos.append(words[0] + " " + words[1] + " " + fixed)
		bb=bb+1
	return typos

fileN = sys.argv[1]
fO = open(fileN[:-4]+"_misspellings.tsv", "w")
dict_clean = pd.read_csv(fileN, sep='\t',encoding = 'utf8',lineterminator='\n',low_memory=False, dtype=str)

for index, row in dict_clean.iterrows():
	missp= butterfinger(row[1])
	for msp in missp:
		fO.write(row[0] + "\t" + msp + "\n")

