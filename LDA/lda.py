#!/usr/bin/env python3
# -*- coding: utf-8 -*

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import nltk
import pandas as pd
import json

import re


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
stop_words = get_stop_words('portuguese', cache=True)
stop_words += get_stop_words('english', cache=True)

# Create pStem of class PorterStemmer
pStem = PorterStemmer()

def readFile():
    with open('twitter/file/result.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        
    return data['text']

def modeling():
    data = readFile()
    texts = []

    for i in data:
        try:
            raw = data[i].lower()
            tokens = tokenizer.tokenize(raw)
            
            tokenStop = [i for i in tokens if not i in stop_words]
            tokenStem = [pStem.stem(i) for i in tokenStop]
            texts.append(tokenStem)
        except:
            continue
    ldaModel(texts)
    
def ldaModel(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word = dictionary, passes=1)
    print(ldamodel.print_topics(num_topics=2, num_words=4))

if __name__ == "__main__":
    modeling()