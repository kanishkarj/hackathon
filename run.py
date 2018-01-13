from bottle import post, run, request
from modules import dbconnector
import threading

conn = dbconnector.dbconnector()

def update():
  t = threading.Timer(10, update)
  t.setDaemon(True)
  t.start()
  conn.update_db()

update()


@post('/')
def hello():
    source = str(request.forms.get('source'))
    title = str(request.forms.get('title'))
    res = conn.db_get(source, title)
    # conn.db_insert("instagram","flower",res)
    return res


run(host='localhost', port=8080, debug=True)
