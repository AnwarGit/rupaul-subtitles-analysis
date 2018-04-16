import string
import sys

import nltk
from nltk.stem import *
import argparse

def main(args):
    """Main function"""
    text_file_path = args.filepath
    stopwords_file_path = args.stopwordsfilepath
    output_file_path = args.outputfilepath

    # Load file and stopwords as taken from command line.
    text_file = open(text_file_path, "r")
    stopwords_file = open(stopwords_file_path, "r")

    # Read text as a string and stopwords as a list
    text = text_file.readlines()
    stopwords = stopwords_file.read().split()

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

    # Write each stemmed token into outputargument in a new line
    outfile = open(output_file_path, 'w')
    for token in text_clean:
        outfile.write(token + "\n")
    outfile.close()


if __name__ == "__main__":
    """Parse args and execute main."""
    parser = argparse.ArgumentParser(description='Preprocess some subtitles.')
    parser.add_argument('--f','filepath', type=str,
                        help='Text file path to preprocess')
    parser.add_argument('--sw','stopwordsfilepath',
                        default = './src/scripts/englishST.txt',
                        help='Stopwords file path to use')
    parser.add_argument('--o','outputfilepath',type=str,
                        default = './allwords_processed.txt',
                        help='Stopwords file path to use')

    args = parser.parse_args()
    main(args)
