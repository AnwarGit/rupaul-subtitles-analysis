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
text = [line.rstrip().lower() for line in text]

text_stopped_1 = []
for line in text:
    for word in line.split():
        if word not in stopwords:
            text_stopped_1.append(word)


text_clean = []
for word in text_stopped_1:
    word_ = word.translate(word.maketrans(string.punctuation, " " * len(string.punctuation)))
    for x in word_.split():
        text_clean.append(x)


text_stopped_2 = []
for word in text_clean:
    if word not in stopwords:
        text_stopped_2.append(word)

text_clean = text_stopped_2
# Write each stemmed token into 'output.txt' in a new line
outfile = open('allwords_processed.txt', 'w')
for token in text_clean:
    outfile.write(token + "\n")
outfile.close()
