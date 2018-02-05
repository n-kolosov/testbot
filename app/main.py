from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Test flask app</h1>'

if __name__ is '__main__':
    app.run()