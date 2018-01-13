from twitterscraper import query_tweets
from ..feed import feed, story

twitter_embed_base = 'https://publish.twitter.com/oembed?url='


def content(tweet):
    if '"' in tweet:
        tweet = '\\"'.join(tweet.split('"'))
    return tweet


def get_feed(page):
    numberofq = 50
    return_data = feed([])
    for tweet in query_tweets(page, numberofq)[:numberofq]:
        url = 'www.twitter.com/' + (tweet.user).lstrip('@') + '/status/' + tweet.id

        ext_url = {'embed_url': twitter_embed_base + url}

        s = story(title=tweet.fullname,
                  pub_time=str(tweet.timestamp),
                  likes=tweet.likes,
                  content=content(tweet.text),
                  url=url,
                  source='Twitter',
                  ext_links=ext_url)

        return_data.append(s)

    return return_data
