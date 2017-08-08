
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'


from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import logging


class Config(object):  
    JOBS = [  
            {  
                'id'        : 'pushQueue',  
                'func'      : 'tticarPushSystem:startPushQueue',  
                'args'      : '',  
                'trigger'   : 'interval',  
                'seconds'   : 10  
            }  
    ]
         
    SCHEDULER_API_ENABLED = True

def initAppConfig(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/push_queue.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
    app.config['STEP_CHECK_PUSH'] = 3
    db = SQLAlchemy(app)
    return db

def initLogging(app):
    handler = logging.FileHandler("mylog", encoding='UTF-8')
    app.logger.addHandler(handler)


def initSchedule(app):
    scheduler = APScheduler()
    app.config.from_object(Config())
    scheduler.init_app(app)
    return scheduler