import csv
from textblob import TextBlob
# import pandas
import glob
from nltk.tokenize import regexp_tokenize
def readfile(filename):
    messages = [line.rstrip() for line in open('SMSSpamCollection.txt')]
    # print (input)
    return messages

filestopwords = open("stopwords.txt").read()

def casefolding(input):
	text = []
	for row in input:
		text.append(row)
	text = [x.lower() for x in text]
	return text

messages = readfile('SMSSpamCollection.txt')
print(messages)
print(casefolding(messages))

training_files = glob.glob('SMSSpamCollection.txt')
for file_name in training_files:
    text = open(file_name, encoding="UTF-8").read()
    filename.append(file_name.split("\\")[1])
    tokens = regexp_tokenize(text, r'[A-Za-z]{3,}')
    data.append(tokens)
