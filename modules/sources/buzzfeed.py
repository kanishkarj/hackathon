import json
import requests
import datetime
from ..feed import feed, story


def get_feed(name):
    r = requests.get('https://www.buzzfeed.com/buzzfeed/search2_json?q='+name)
    data = json.loads(r.text)
    final_feed = feed([])
    for t in data['response']['results']:
        _time=datetime.datetime.fromtimestamp(int(t['published_unix'])).strftime('%Y-%m-%d %H:%M:%S')
        new_story = story('buzzfeed'+'-'+name,title=t['name'], pub_time=_time,
                          content=t['blurb'], url=t['link'],
                          source='buzzfeed', ext_links=t['m_image'])
        final_feed.append(new_story)
    return final_feed
