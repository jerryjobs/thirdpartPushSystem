#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'


from push.push_config import testMiPush

from api.db_model import PushQueue

if __name__ == '__main__':
    print('------------start test----------------')
    pq = PushQueue(None, 'target', 'mi', 'A title for push ', 'this is a test content')
    testMiPush(pq)
    print('---------------- end -----------------')