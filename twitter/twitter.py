# -*- coding: utf-8 -*

import tweepy as tw
import pandas as pd

# Method for authantication with twitter
def auth():
    with open('file/tokens.txt', 'r') as tfile:
        consumer_key = tfile.readline().strip('\n')
        consumer_secret = tfile.readline().strip('\n')
        access_token = tfile.readline().strip('\n')
        access_token_secret = tfile.readline().strip('\n')
        
    auth_user = tw.OAuthHandler(consumer_key, consumer_secret)
    auth_user.set_access_token(access_token, access_token_secret)

    api = tw.API(auth_user)
    return api

# Method for get message of twitter
def getMessage():
    api = auth()
    
    querySearch = '#CORONAVIRUS #COVID19 ' + '-filter:retweet'
    tweets = tw.Cursor(api.search, q=querySearch).items(100)
    
    # Creating directory
    tweetsDict = {}
    twkey = {'text': None, 'created_at': None, 'entities': None, 'lang': None}
    tweetsDict = tweetsDict.fromkeys(twkey)
    
    for tweet in tweets:    
        for key in tweetsDict.keys():
            try:
                twKey = tweet._json[key]
                tweetsDict[key].append(twKey)
            except KeyError:
                twKey = ""
                tweetsDict[key].append("")
            except:
                tweetsDict[key] = [twKey]
    dfTweets = pd.DataFrame.from_dict(tweetsDict)
    dfTweets.head()
    dfTweets.to_json('file/result.json')

# Main
if __name__ == '__main__':
    getMessage()