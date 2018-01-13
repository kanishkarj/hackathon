from bottle import post, run, request
from modules import dbconnector

conn = dbconnector.dbconnector()


@post('/')
def hello():
    source = str(request.forms.get('source'))
    title = str(request.forms.get('title'))
    res = conn.db_get(source, title)
    # conn.db_insert("instagram","flower",res)
    # conn.update_db()
    return res


run(host='localhost', port=8080, debug=True)
