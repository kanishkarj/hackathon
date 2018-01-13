from bottle import route, run, request
from modules import dbconnector
import threading

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

conn = dbconnector.dbconnector()

def update():
  t = threading.Timer(10, update)
  t.setDaemon(True)
  t.start()
  conn.update_db()

update()


@route('/')
def hello():
    source = str(request.query.get('source'))
    title = str(request.query.get('title'))
    print(source)
    print(title)
    res = conn.db_get(source, title)
    # conn.db_insert("instagram","flower",res)
    return res


run(host='localhost', port=8080, debug=True)
