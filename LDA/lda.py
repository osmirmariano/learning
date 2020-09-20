#!/usr/bin/env python3
# -*- coding: utf-8 -*

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pandas as pd
import json

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

def readFile():
    with open('twitter/file/result.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        
    return data['text']

def modeling():
    data = readFile()
    # texts = []

    for i in data:
        raw = data[i].lower()
        tokens = tokenizer.tokenize(raw)
        print(tokens)

if __name__ == "__main__":
    modeling()