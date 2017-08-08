from flask import Flask
from flask import render_template as render
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
import logging
from flask_apscheduler import APScheduler

app = Flask(__name__)

from config.db_config import initAppConfig
from config.db_config import initLogging
from config.db_config import initSchedule
from config.db_config import Config

db = initAppConfig(app)
initLogging(app)
#scheduler = initSchedule(app)
app.config.from_object(Config())

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

@app.route('/push/list_all', methods=['GET'])
def list_all():
    pageSize = 10
    page = 0
    if request.args :
        try:
            if request.args.get('pageSize') :
                pageSize = int(request.args.get('pageSize'))
        
            if request.args.get('page') :
                page = int(request.args.get('page'))
        except(Exception):
            return ""
    page = page - 1
    if page < 0 :
        page = 0
    #print(page, pageSize)
    from api.db_model import PushQueue
    result = PushQueue.query.order_by(PushQueue.id.desc()).offset(pageSize * page).limit(pageSize).all()
    return render('list_all.html', result=result, nextPage=page+2, prevPage= page-1)

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

#@app.route('/api/start_push_queue', methods=['GET'])
def startPushQueue():
    '''
    start push queue from list
    '''
    from jobs import startQueue as queueThread
    queueThread()
    # blsch.scheduled_job(queueThread, 'interval',seconds=10)
    # blsch.start()
    return '1'

if __name__ == '__main__':
    from push import getui  
    from push import mipush

    print( getui.packageInfo)
    print (mipush.packageInfo)
    
    # logging.info('init push service  loop')
    # app.logger.info('init push service  loop')
    # app.logger.debug('init push service ....')
    # from api.db_model import PushQueue
    #startPushQueue()
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)
