#!python3
from twitterscraper import query_tweets
import json

def content(tweet):
    if '"' in tweet:
        tweet = '\\"'.join(tweet.split('"'))
    return tweet

def generatejson(tag, location):
    numberofq=50
    jsonfile=[]
    for tweet in query_tweets(tag+" AND Blockchain near:" + location, numberofq)[:numberofq]:
 #   for tweet in query_tweets(tag, 10)[:numberofq]:
        jsonfile.append({"title":tweet.fullname,
         "published" : str(tweet.timestamp),
         "likes" : tweet.likes,
         "content" : content(tweet.text),
         "url" : 'www.twitter.com/' + (tweet.user).lstrip('@') + '/status/' + tweet.id,
         "source":'Twitter'})
    
    if len(jsonfile)>50:
        jsonfile=jsonfile.sort(key=lambda x: x["likes"])
    with open('twitter.json', 'w') as outfile:
        json.dump(jsonfile, outfile)

generatejson(tag='Food', location='India')
#generatejson(tag='football')
