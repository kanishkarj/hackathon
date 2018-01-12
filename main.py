from importlib import import_module

def get_feed(sm, name):
    social_media = import_module(sm)
    feed = social_media.get_feed(name)
    return feed
