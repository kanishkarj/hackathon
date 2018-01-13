import requests
from ..feed import feed, story


def get_feed(name):
    r = requests.get("https://9gag.com/v1/featured-posts?pageType=" + name)
    assert r.status_code == 200
    # parse data
    final = feed([])
    data = r.json()
    data = data['data']['items']
    maxcount = 50
    count = 0
    for i in data:
        if count >= maxcount:
            break
        print(i)
        new_story = story(i['url'], '', '', i['title'], '9gags', {
                          'photo': ['i.imageURL']}, i['upVoteCount'])
        final.append(new_story)
    return final
