from bottle import route, run, template

@route('/hello')
def hello():
    return template('home')


run(host='localhost', port=8080, debug=True)
