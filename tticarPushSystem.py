from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return u'Welcome to 天天爱车推送系统.'


if __name__ == '__main__':
    app.run()
