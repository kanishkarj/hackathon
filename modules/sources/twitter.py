from twitterscraper import query_tweets
from ..feed import feed, story
import urllib.request
import urllib.parse

twitter_embed_base = 'https://publish.twitter.com/oembed?url='


def content(tweet):
    if '"' in tweet:
        tweet = '\\"'.join(tweet.split('"'))
    return tweet


def get_feed(page):
    numberofq = 50
    return_data = feed([])
    for tweet in query_tweets(page, numberofq)[:numberofq]:
        base_url = "http://www.twitter.com"
        ext_url = {'embed_url': twitter_embed_base + base_url + tweet.url}


        s = story(title=tweet.fullname,
                  pub_time=str(tweet.timestamp),
                  likes=tweet.likes,
                  content=content(tweet.text),
                  url=base_url+tweet.url,
                  source='Twitter',
                  id='twitter'+'-'+page,
                  ext_links=ext_url)

        return_data.append(s)

    return return_data
