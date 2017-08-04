from flask import Flask
from flask import render_template as render

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render(
        'index.html',
        title='多推送系统',
        version='0.1'
    )




if __name__ == '__main__':
    app.run(debug = True)
