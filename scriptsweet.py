from nltk.corpus import stopwords
from collections import Counter
import re
from collections import OrderedDict
import csv
from stemming.porter2 import stem

filestopwords = open("stopwords.txt").read()
stopword = filestopwords.split("\n")

fileslang = open("slang-words.txt").read()
slang = []
slang2 = fileslang.split("\n")
for line in slang2 :
	slang.append(line.split("`"))

def replaceword(word):
	for line in slang:
		if(word==line[0]):
			return line[1]
	return word

def readfile(filename):

	input = csv.reader(open(filename,'r', encoding='utf-8', errors='ignore').readlines())
	return input

def preprocessing(text):
	textpre = []
	# text = " ".join(text).split()
	for sentence in text:
		sentence = re.sub('&(\w*);', '', sentence)  # clear &quot;
		sentence = re.sub('(http\:\/\/)?(http\:\/\/|www).(\w)*.[\w/.\-\?]*', 'link', sentence) #change link www to 'link'
		# print("SENTENCE : ", sentence)
		tmp = []
		for line in sentence.lower().split() :
			if line not in stopword : #jk dia bukan stopword,mk masuk ke array
				tmp.append(replaceword(line))
		# textpre = ' '.join([sen for sen in sentence if sen not in stopwords.words("english")])
		textpre.append(tmp)
	return  textpre

textinput = readfile('smsspamcoll.csv')
print("==== DATA TRAINING ====")
# print(textinput)
print("\n == CASE FOLDING ==")

smsspam = []
smsham = []
for row in textinput:
	if(row[0]=="spam"):
		smsspam.append(row[1])
	else:
		smsham.append(row[1])
smsham = [x.lower() for x in smsham]
smsspam = [x.lower() for x in smsspam]
# print("SMS SPAM = \n",smsspam)
# print("SMS BUKAN SPAM = \n",smsham)

print("\n PREPROCESSING SMS SPAM:: ",preprocessing(smsspam))


