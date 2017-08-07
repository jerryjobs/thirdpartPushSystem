
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'


from flask_sqlalchemy import SQLAlchemy

def initAppConfig(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/push_queue.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
    db = SQLAlchemy(app)
    return db