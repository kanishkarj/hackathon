from bottle import route, run, template
from modules import main,dbconnector
import json

@route('/')
def hello():
    res = main.get_feed("facebook","pclubiiti")
    # conn = dbconnector.dbconnector()
    # conn.db_insert("instagram","flower",res)
    return template('home')

run(host='localhost', port=8080, debug=True)
