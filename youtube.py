from feed import feed, story
from urllib.parse import urlencode
from urllib import request
import json
import re


def get_feed(name):
    uploads = get_channel_uploads(name)
    youtube_videos = feed([])
    for item in uploads['items']:
        s = return_story(item)
        youtube_videos.append(story=s)

    return youtube_videos


def call_gdata(api, qs):
    qs = dict(qs)
    qs['key'] = 'AIzaSyDvysm00R5FClmqtxcATsgpKHdt2GxCaiU'
    url = 'https://www.googleapis.com/youtube/v3/' + api + '?' + urlencode(qs)

    data = request.urlopen(url).read().decode('utf-8')

    return json.loads(data)


def get_channel_uploads(url):
    query = None
    chanR = re.compile('.+channel\/([^\/]+)$')
    userR = re.compile('.+user\/([^\/]+)$')
    channel_id = None
    channel_url = url
    if chanR.match(channel_url):
        channel_id = chanR.search(channel_url).group(1)
    elif userR.match(channel_url):
        username = userR.search(channel_url).group(1)
        query = {'part': 'snippet, contentDetails, statistics',
                 'forUsername': username}
    elif len(channel_url) == 24 and channel_url[:2] == 'UC':
        channel_id = channel_url
    else:
        username = channel_url
        query = {'part': 'snippet, contentDetails, statistics',
                 'forUsername': username}

    if query is None:
        query = {'part': 'snippet, contentDetails, statistics',
                 'id': channel_id}
    allinfo = call_gdata('channels', query)

    try:
        ch = allinfo['items'][0]
    except IndexError:
        err = "Unrecognized channel id, url or name : %s"
        raise ValueError(err % channel_url)

    return get_uploads(ch['contentDetails']['relatedPlaylists']['uploads'])


def get_uploads(upload_id):
    query = {'part': 'snippet',
             'maxResults': 50,
             'playlistId': upload_id}

    data = call_gdata('playlistItems', query)

    return data


def return_story(item):
    s = story(url='www.youtube.com/watch?v='+item['snippet']['resourceId']['videoId'],
              title=item['snippet']['title'],
              pub_time=parseISO8591(item['snippet']['publishedAt']),
              content=item['snippet']['description'],
              source='youtube',
              ext_links=[])

    return s


def parseISO8591(duration):
    """ Parse ISO 8591 formated duration """
    regex = re.compile(r'PT((\d{1,3})H)?((\d{1,3})M)?((\d{1,2})S)?')
    if duration:
        duration = regex.findall(duration)
        if len(duration) > 0:
            _, hours, _, minutes, _, seconds = duration[0]
            duration = [seconds, minutes, hours]
            duration = [int(v) if len(v) > 0 else 0 for v in duration]
            duration = sum([60**p*v for p, v in enumerate(duration)])
        else:
            duration = 30
    else:
        duration = 30
    return duration
