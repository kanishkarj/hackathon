from bottle import post, run, template,request
from modules import dbconnector
import json

conn = dbconnector.dbconnector()

@post('/')
def hello():
    source = str(request.forms.get('source'))
    title = str(request.forms.get('title'))
    res = conn.db_get(source,title)
    # conn.db_insert("instagram","flower",res)
    # conn.update_db()
    return res

run(host='192.168.2.226', port=8080, debug=True)
