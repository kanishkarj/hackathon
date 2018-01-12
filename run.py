from bottle import route, run, template
from modules.sources.facebook import scrapeFacebookPageFeedStatus

app_id = "542979522719768"
app_secret = "c1dfb166b76b79bd19f3ca811bea1aba"  # DO NOT SHARE WITH ANYONE!
page_id = "pclubiiti"

# input date formatted as YYYY-MM-DD
since_date = ""
until_date = ""

access_token = app_id + "|" + app_secret

@route('/')
def hello():
    res = scrapeFacebookPageFeedStatus(page_id,access_token,since_date,until_date)
    return template('home')


run(host='localhost', port=8080, debug=True)
