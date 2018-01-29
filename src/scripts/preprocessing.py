import string
import sys

import nltk
from nltk.stem import *

# Load file and stopwords as taken from command line.
textfile = open(sys.argv[1], "r")
stopwordsfile = open(sys.argv[2], "r")

# Read text as a string and stopwords as a list
text = textfile.readlines()
stopwords = stopwordsfile.read().split()

# Case folding & remove stopwords
text_rstripped = [line.lower().rstrip() for line in text]

text_stopped = []
for line in text_rstripped:
    line_clean = [word for word in line.split() if (word not in stopwords)]
    for word in line_clean:
        text_stopped.append(word)


text_clean = []
for word in text_stopped:
    word_ = word.translate(word.maketrans(string.punctuation, " " * len(string.punctuation)))
    text_clean.append(word_)



# print("Length of token list:\t", len(tokens))  # DEBUG



# print("Stopwords removed from token list.")  # DEBUG
# print("Length of token list after stopwords removal:\t", len(tokens))  # DEBUG

# Stemming
#stemmer = PorterStemmer()
#stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Write each stemmed token into 'output.txt' in a new line
outfile = open('allwords_processed.txt', 'w')
for token in text_clean:
    outfile.write(token + "\n")
outfile.close()
