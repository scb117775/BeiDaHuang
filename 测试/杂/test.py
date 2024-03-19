from flask import Flask

app = Flask(__name__)

@app.route('/')
def h():
    return 'succeed'

@app.route('/hello')
def hello():
    return 'hello word!'

if __name__ == '__main__':
    app.run(port = 8080)
