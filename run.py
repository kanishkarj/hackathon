from bottle import route, run, request
from modules import dbconnector

conn = dbconnector.dbconnector()


@route('/')
def hello():
    source = str(request.query.get('source'))
    title = str(request.query.get('title'))
    print(source)
    print(title)
    res = conn.db_get(source, title)
    # conn.db_insert("instagram","flower",res)
    # conn.update_db()
    return res


run(host='192.168.2.226', port=8080, debug=True)
