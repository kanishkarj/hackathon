import json


class story:
    def __init__(self, url, title, pub_time, content, source, ext_links=[], likes=None):
        self.title = title
        self.published = pub_time
        self.content = content
        self.url = url
        self.source = source
        self.ext_links = ext_links  # ext_links is a list
        self.likes = likes


class feed:
    def __init__(self, stories):
        self.stories = stories
        self.__iter__ = self.stories.__iter__

    def __getitem__(self, index):
        return self.stories[index]

    def append(self, story):
        self.stories.append(story)

    def extend(self, feed):
        self.stories.extend(feed)

    def sortByTime(self):
        pass

    def sortByPopularity(self):
        pass

    def toJson(self):
        return ','.join(json.dumps(x.__dict__) for x in self.stories)
