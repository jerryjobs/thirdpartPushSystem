from flask import Flask
from flask import render_template as render
from flask.ext.wtf import Form

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render(
        'index.html',
        title='多推送系统',
        version='0.1'
    )

@app.route('/push/info')
def push_info():
    return render('push_info.html')


if __name__ == '__main__':
    from push import getui
    from push import mipush

    app.run(debug = True)
