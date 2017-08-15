#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'


from push.push_config import testMiPush

from push.huawei import HuaWeiPush

from api.db_model import PushQueue

if __name__ == '__main__':
    print('------------start test----------------')
    pq = PushQueue(None, 'target', 'mi', 'A title for push ', 'this is a test content')
    #testMiPush(pq)
    huaweiPush = HuaWeiPush()
    pqHuawei = PushQueue(None, '0861012037486274300000742500CN01', 'huawei', 'A title for push ', 'this is a test content')
    huaweiPush.send_push(pqHuawei)

    print('---------------- end -----------------')