import urllib.request
import urllib.parse
import json

from ..feed import feed, story

base_url = 'https://www.instagram.com/graphql/query/?query_id=17886322183179102&'


def get_feed(name):
    query = 'variables=%7B"tag_name":"' + name + '","first":12%7D'
    url = base_url + query

    try:
        r = urllib.request.urlopen(url)
    except:
        raise

    data = json.loads(r.read())
    data = data['data']['hashtag']['edge_hashtag_to_media']['edges']

    return_data = feed([])
    for item in data:
        s = story_from_dict(item,name)
        return_data.append(s)

    return return_data


def story_from_dict(item,name):
    try:
        content = item['node']['edge_media_to_caption']['edges'][0]['node']['text']
    except:
        content = ''

    try:
        ext_links = {'photo': item['node']['display_url']}
    except:
        ext_links = {'video': item['node']}
    return story(url='https://www.instagram.com/p/'+item['node']['shortcode'],
                 title='',
                 pub_time=item['node']['taken_at_timestamp'],
                 content=content,
                 source='instagram',
                 id='instagram'+'-'+name,
                 likes=item['node']['edge_liked_by']['count'],
                 ext_links=ext_links
                 )
