from instaloader import Instaloader
from feed import feed, story


def get_feed():
    loader = Instaloader()
    final_feed = feed([])
    x = loader.get_hashtag_posts("flowers")
    maxcount = 10
    count = 0
    for i in x:
        count += 1
        if count > maxcount:
            break
        ext = {}
        if i.is_video:
            ext['video'] = i.video_url
        else:
            ext['photo'] = i.url
        new_story = story("https://instagram.com/p/{}".format(i.shortcode),
                          "", str(i.date), i.caption, "Instagram", ext)
        final_feed.append(new_story)
    return final_feed
