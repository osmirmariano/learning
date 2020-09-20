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
enStop = get_stop_words('en')

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
        raw = data[i].lower()
        tokens = tokenizer.tokenize(raw)

        tokenStop = [i for i in tokens if not i in enStop]
        
        tokenStem = [pStem.stem(i) for i in tokenStop]

        texts.append(tokenStem)
    
    ldaModel(texts)
    

def ldaModel(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
    print(ldamodel.print_topics(num_topics=2, num_words=4))

if __name__ == "__main__":
    modeling()