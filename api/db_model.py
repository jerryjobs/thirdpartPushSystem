# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'

from tticarPushSystem import db
from tticarPushSystem import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime


class PushQueue(db.Model):
    '''
    this is the queue of push . 
    '''
    __tablename__ = 'push_queue'

    id = Column(Integer, primary_key=True)
    target = Column(String)
    pushType = Column(String)
    title = Column(String)
    content = Column(String)
    createTime = Column(DateTime)
    sendTime = Column(DateTime)
    isArrive = Column(Boolean)


    def __init__(self, id, target, pushType, title, content):
        #self.id, self.target, self.pushType, self.title, self.content createTime, self.sendTime = (id, target, pushType, title, content, createTime, sendTime)
        self.id = id
        self.target = target
        self.pushType = pushType
        self.title = title
        self.content = content
        self.createTime = datetime.utcnow()
        self.sendTime = None
        self.isArrive = False
        
    def __repr__(self):
        return "<PushQueue(id='%s', title='%s', content='%s', createTime='%s', sendTime='%s', isArrive='%s'>" % (self.id, self.title, self.content, self.createTime, self.sendTime, self.isArrive)


def save(obj):
    db.session.add(obj)
    db.session.commit()

db.create_all()