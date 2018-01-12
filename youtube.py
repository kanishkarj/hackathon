import youtube_channel
from feed import feed, story
from urllib import urlencode
from urllib import request


def get_feed(name):
    channel = youtube_channel.get_channel(name)
    uploads = channel.uploads
    youtube_videos = feed([])
    i = 0
    for x in uploads:
        s = story(url=x.watchv_url,
                  title=x.title,
                  pub_time=x.published,
                  content=x.description,
                  source='youtube',
                  ext_links=[])
        youtube_videos.append(story=s)
        i += 1
        if i == 50:
            break

    return youtube_videos


def call_gdata(api, qs):
    qs = dict(qs)
    qs['key'] = 'AIzaSyDvysm00R5FClmqtxcATsgpKHdt2GxCaiU'
    url = 'https://www.googleapis.com/youtube/v3/' + api + '?' + urlencode(qs)

    try:
        data = request.urlopen(url).read().decode('utf-8')
    except HTTPError as e:
        raise

    return json.loads(data)
