from bottle import route, run, template

@route('/')
def hello():
    return template('home')


run(host='localhost', port=8080, debug=True)
