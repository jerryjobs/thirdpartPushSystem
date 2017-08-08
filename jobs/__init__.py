from tticarPushSystem import db
import time
from api.db_model import PushQueue
import threading
from datetime import datetime
import logging

class PushThread(threading.Thread):

    def __init__(self, pushQueue):
        self.queueItem = pushQueue
        threading.Thread.__init__(self) 

    def run(self):
        logging.log(logging.INFO, 'push a message %s' % self.queueItem)
        self.sendPush()
        print('in thread loop')

    def sendPush(self):
        pq = PushQueue.query.filter_by(id=self.queueItem.id).first()
        print(pq)
        if pq :
            pq.sendTime = datetime.utcnow()
            print(pq)
            db.session.commit()

def loop(stepSeconds):
    '''
    启动自检测，每过N秒检测一次 如果有未发送的push 就启动一个线程准备发送这条push
    '''
    if isinstance(stepSeconds, int) is False:
        raise Exception('setp must be a int number')

    while(True):
        time.sleep(5)
        result = PushQueue.query.filter('sendTime ISNULL') \
        .order_by(PushQueue.id.desc()).offset(0).limit(9).all()

        if result :
            for item in result:
                pt = PushThread(item)
                pt.start()
        else:
            
            pass
        #pt = PushThread()
    pass