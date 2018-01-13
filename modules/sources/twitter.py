from twitterscraper import query_tweets
import json
from ..feed import feed, story


def content(tweet):
    if '"' in tweet:
        tweet = '\\"'.join(tweet.split('"'))
    return tweet


def get_feed(page):
    numberofq = 50
    return_data = feed([])
    for tweet in query_tweets('Blockchain from:'+ page, numberofq)[:numberofq]:
        s = story(title=tweet.fullname,
                  pub_time=str(tweet.timestamp),
                  likes=tweet.likes,
                  content=content(tweet.text),
                  url='www.twitter.com/' + (tweet.user).lstrip('@') + '/status/' + tweet.id,
                  source='Twitter')

        return_data.append(s)

    return return_data

