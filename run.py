from bottle import route, run, template
from modules import main

@route('/')
def hello():
    res = main.get_feed("facebook","pclubiiti")
    return template('home')


run(host='localhost', port=8080, debug=True)
