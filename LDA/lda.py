#!/usr/bin/env python3
# -*- coding: utf-8 -*
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pandas as pd
import json
import re


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
stop_words = get_stop_words('portuguese', cache=True)
stop_words += get_stop_words('english', cache=True)

# Create pStem of class PorterStemmer
pStem = PorterStemmer()

"""
Função para ler arquivo e processar os dados
"""
def readFile():
    with open('twitter/file/result.json', 'r', encoding='utf8') as f:
        data = json.load(f)

    return data['text']

"""
Função remover caracteres especiais
"""
def removeCharacter(listWord):
    newList = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in listWord]
    result = [] 
    for val in newList: 
        if val != '' : 
            result.append(val)
    return result

"""
Função para modelagem dos dados e remover termos
"""
def modeling():
    data = readFile()
    texts = []

    for i in data:
        try:
            raw = data[i].lower()
            tokens = tokenizer.tokenize(raw)
            
            listWords = removeCharacter(tokens)
            tokenStop = [i for i in listWords if not i in stop_words]
            tokenStem = [pStem.stem(i) for i in tokenStop]
            texts.append(tokenStem)
        except:
            continue
    ldaModel(texts)

"""
Função o LDA e mostrar os dados
"""
def ldaModel(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word = dictionary, passes=1)
    print(ldamodel.print_topics(num_topics=2, num_words=10))


if __name__ == "__main__":
    modeling()