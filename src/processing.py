
import os
import re
import sys
import xml
import json

from . import readSubtitles as rs

class Collection():
    def __init__(self,path):
        self.path = path
        self.name = path.split('/')[-1]

    def allwords(self,verbose=True):
        output_file = open(self.path+'/allwords.txt','w')
        if verbose:
            print('Saving all words in '+ self.path+'/allwords.txt')

        for subtitle_path in os.listdir(self.path):
            subtitle = rs.superSubtitle(self.path + "/" + subtitle_path)
            if subtitle.extension not in ['srt','sub','txt','tmp','smi','ssa']:
                continue #DEBUG
                raise ValueError('Subtitle extension \''+subtitle.extension+'\' not compatible with superSubtitle. Supersubtitle can only read .srt, .sub, .txt, .tmp, .smi, .ssa subtitles.')
            subtitle_text = subtitle.toText()
            output_file.write(subtitle_text+"\n\n")

            if verbose:
                print('Processed '+ subtitle.name)
        output_file.close()
        if verbose:
            print('Finished.')

def joinAllwords(overall_path):
    allwords_overall = open('allwords_allseasons.txt','w')

    for season in os.listdir(overall_path):
        if season.startswith('.DS_S'):
            continue
        allwords = open(overall_path+'/'+season+'/allwords_clean.txt','r')

        allwords_overall.write(allwords.read())

    allwords_overall.close()
