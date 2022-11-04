from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    return 'Testing...1,2,3'