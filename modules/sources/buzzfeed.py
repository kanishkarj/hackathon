import json
import requests
from ..feed import feed, story


def get_feed(name):
    r = requests.get('https://www.buzzfeed.com/buzzfeed/search2_json?q='+name)
    data = json.loads(r.text)
    final_feed = feed([])
    for t in data['response']['results']:
        new_story = story(title=t['name'], pub_time=t['published_unix'],
                          content=t['blurb'], url=t['link'],
                          source='buzzfeed', ext_links=t['m_image'])
        final_feed.append(new_story)
    return final_feed
