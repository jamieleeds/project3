# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

nltk.download('book')
from nltk.book import * 

from nltk import word_tokenize,sent_tokenize

debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")
fname = "madlibtest2.txt" # need a file with this name in directory

tokens = text2[:151]

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

print("".join([spaced(word) for word in tokens])) #1 printing out 150 tokens of the original text 


tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PP": "a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "PP": .10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))





print("\n\nEND*******")