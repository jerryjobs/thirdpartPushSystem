from flask import Flask
from flask import render_template as render
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
import logging

app = Flask(__name__)

from config.db_config import initAppConfig
from config.db_config import initLogging
db = initAppConfig(app)
initLogging(app)

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

@app.route('/api/insertpush', methods=['PUT'])
def insert_push():
    '''
    this is remote app call insert a push message
    METHOD : PUT
    params {
        target : push clinet id,
        pushType : (mi, huawei, getui)
        title: push message title
        content: push message content
    }
    '''
    if request.method == 'PUT':
        if request.form :
            if request.form['target'] and request.form['pushType'] \
            and request.form['title'] and request.form['content'] :
                from api.db_model import PushQueue
                pq = PushQueue(None, request.form['target'], request.form['pushType'], request.form['title'], request.form['content'])
                print(pq)
                db.session.add(pq)
                db.session.commit()
                return '1'

    return '0'


if __name__ == '__main__':
    from push import getui
    from push import mipush

    print( getui.packageInfo)
    print (mipush.packageInfo)
    
    logging.info('init push service  loop')
    app.logger.info('init push service  loop')
    app.logger.debug('init push service ....')
    from jobs import loop as pushServiceLoop
    from api.db_model import PushQueue
    #print(dir(db.session))
    #exit()
    
    pushServiceLoop(app.config['STEP_CHECK_PUSH'])
    
    app.run(debug=True)
