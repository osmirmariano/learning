# -*- coding: utf-8 -*
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY= ''
ACCESS_TOKEN_SECRET= ''

import twitter

def auth():
    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    
    return api

def get_message():
    api = auth()
    response = api.GetSearch(term='CBLoL')
    for i in response:
        print(i)

if __name__ == '__main__':
    get_message()