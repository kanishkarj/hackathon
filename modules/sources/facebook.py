import json
import datetime
import time

from ..feed import feed, story
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

app_id = "542979522719768"
app_secret = "c1dfb166b76b79bd19f3ca811bea1aba"  # DO NOT SHARE WITH ANYONE!

access_token = app_id + "|" + app_secret


def get_feed(name):
    res = scrapeFacebookPageFeedStatus(name, access_token, '', '')
    data = feed([])
    i = 0

    try:
        res = res['data']
    except:
        pass

    print(res[0])
    print(res[0].keys())

    for x in res:
        if 'link' not in x or 'message' not in x:
            continue

        ext_links['embed_url'] = "https://www.facebook.com/plugins/post.php?href={0}&width=500&show_text=true&height=472&appId".format(x['link'])
        s = story(url= x['link'],
                  title='',
                  pub_time=x['created_time'].replace("+0000", "").replace("T", " "),
                  content=x['message'],
                  source='facebook',
                  ext_links=ext_links)
        data.append(s)
        i += 1
        if i >= 50:
            break

    return data


def request_until_succeed(url):
    req = Request(url)
    success = False
    while success is False:
        try:
            response = urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL {}: {}".format(url, datetime.datetime.now()))
            print("Retrying.")

    return response.read()


# Needed to write tricky unicode correctly to csv
def unicode_decode(text):
    try:
        return text.encode('utf-8').decode()
    except UnicodeDecodeError:
        return text.encode('utf-8')


def getFacebookPageFeedUrl(base_url):

    # Construct the URL string; see http://stackoverflow.com/a/37239851 for
    # Reactions parameters
    fields = "&fields=message,link,created_time,type,name,id," + \
        "comments.limit(0).summary(true),shares,reactions" + \
        ".limit(0).summary(true)"

    return base_url + fields


def scrapeFacebookPageFeedStatus(page_id, access_token, since_date, until_date):

    reaction_types = ['like', 'love', 'wow', 'haha', 'sad', 'angry']
    has_next_page = True
    num_processed = 0
    scrape_starttime = datetime.datetime.now()
    after = ''
    base = "https://graph.facebook.com/v2.9"
    node = "/{}/posts".format(page_id)
    parameters = "/?limit={}&access_token={}".format(100, access_token)
    since = "&since={}".format(since_date) if since_date \
        is not '' else ''
    until = "&until={}".format(until_date) if until_date \
        is not '' else ''

    #print("Scraping {} Facebook Page: {}\n".format(page_id, scrape_starttime))

    while has_next_page:
        after = '' if after is '' else "&after={}".format(after)
        base_url = base + node + parameters + after + since + until

        url = getFacebookPageFeedUrl(base_url)
        statuses = json.loads(request_until_succeed(url))


        # if there is no next page, we're done.
        if 'paging' in statuses:
            after = statuses['paging']['cursors']['after']
        else:
            has_next_page = False

        return statuses

    print("\nDone!\n{} Statuses Processed in {}".format(
          num_processed, datetime.datetime.now() - scrape_starttime))
