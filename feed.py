class story:
    def __init__(self, url, title, pub_time, content, source, ext_links=[]):
        self.title = title
        self.published = pub_time
        self.content = content
        self.url = url
        self.source = source
        self.ext_links = ext_links  # ext_links is a list


class feed:
    def __init__(self, stories):
        self.stories = stories

    def append(self, story):
        self.stories.append(story)

    def extend(self, feed):
        self.stories.extend(feed)

    def sortByTime(self):
        pass

    def sortByPopularity(self):
        pass
