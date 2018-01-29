import string
import sys

import nltk
from nltk.stem import *

# Load file and stopwords as taken from command line.
textfile = open(sys.argv[1], "r")
stopwordsfile = open(sys.argv[2], "r")

# Read text as a string and stopwords as a list
text = textfile.read()
stopwords = stopwordsfile.read().split()

# Case folding & remove punctuation
text = text.lower()
text = text.translate(text.maketrans(
    string.punctuation, " " * len(string.punctuation)))

# Tokenization
tokens = text.split()
# print("Length of token list:\t", len(tokens))  # DEBUG

# Stopping
tokens = [token for token in tokens if token not in stopwords]

# print("Stopwords removed from token list.")  # DEBUG
# print("Length of token list after stopwords removal:\t", len(tokens))  # DEBUG

# Stemming
#stemmer = PorterStemmer()
#stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Write each stemmed token into 'output.txt' in a new line
outfile = open('allwords_processed.txt', 'w')
for token in tokens:
    outfile.write(token + "\n")
outfile.close()
