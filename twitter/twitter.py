#!/usr/bin/env python3
# -*- coding: utf-8 -*

import twitter

def auth():
    api = twitter.Api(
        consumer_key='',
        consumer_secret='',
        access_token='',
        access_token_secret=''
    )
    return api

def getMessage():
    api = auth()
    response = api.GetSearch(term='')
    for i in response:
        print(i)

if __name__ == '__main__':
    getMessage()