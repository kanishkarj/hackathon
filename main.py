from importlib import import_module

def get_feed(sm):
    social_media = import_module()
    feed = social_media.get_feed()
    return feed
