# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'

from sqlalchemy import Column, String, create_engine, Integer, Text, MetaData, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

prePath = 'push_queue.db'

engine = create_engine("sqlite:///%s" % prePath, echo=True)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)

class PushQueue(Base):
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
    def __repr__(self):
        return "<PushQueue(id='%s', title='%s', content='%s', createTime='%s', sendTime='%s', isArrive='%s'>" % (self.id, self.title, self.content, self.createTime, self.sendTime, self.isArrive)


def userDb(func):
    '''

    :param func:
    :return:
    '''
    session = DBSession()
    def wrapper(*args, **kwargs):
        print('saved a session : %s' % kwargs.keys())
        kwargs['session'] = session
        return func(*args, **kwargs)
    session.close()

    return wrapper

@userDb
def insert_queue(queue, session=None):

    if queue is None:
        raise Exception('type must be Gallery')

    if session is None:
        raise Exception('session can not be None')

    session.add(queue)
    session.commit()
    return queue


Base.metadata.create_all(engine)

def test():
    '''
    test insert and init db.
    '''
    pQueue = PushQueue()
    pQueue.id = None
    pQueue.title = "test"
    pQueue.content = "WOW"
    print(pQueue)
    insert_queue(pQueue)
    pass

if __name__ == '__main__':
    #test()
    pass
    # result = query_gallery()
    # for item in result:
    #     print(item)

    # print(dir(Gallery.metadata.tables))


    # gallery = Gallery(name = 'jerry', link = 'http://www.baidu.com')
    # galleryMan = insert_gallery(gallery= gallery)
    # print(galleryMan)

    # gallery_content = GalleryContent(gallery_id=1, url='test', size=0, width=0, height=0)
    # insert_gallery_item(gallery_item=gallery_content)



