#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'

import os

class PushSupport() :
    pass


class Getui():

    _APPKEY = 'EtNTKPQiYa7GOv10T6Awd6'
    _APPID = 'ZX7GLsMsicA2qlTqZHlG81'
    _MASTERSECRET = "zXAbgylpNc80hq7NwlHiu3"
    _CID = ''
    _Alias = ''
    _DEVICETOKEN = ''
    # http的域名
    _HOST = 'http://sdk.open.api.igexin.com/apiex.htm'

    def __init__(self):
        os.environ['needDetails'] = 'true'
        pass
        # from .getui.igt_push import IGeTui
        # self.pushService = IGeTui(self._HOST, self._APPKEY, self._MASTERSECRET)
        
    def sendTransmissionMessage(self, pushItem):
        '''
        发送一条透传消息
        '''
        pass

    def sendNotifycation(self, pushItem):
        """
        发送一个通知    参数为一条 消息实体
        """
        # 消息模版： 
        # 1.TransmissionTemplate:透传功能模板  
        # 2.LinkTemplate:通知打开链接功能模板  
        # 3.NotificationTemplate：通知透传功能模板  
        # 4.NotyPopLoadTemplate：通知弹框下载功能模板

        # template = NotificationTemplate()

        # template.transmissionType = 1
        # template.appId = self._APPID
        # template.appKey = self._APPKEY
        # template.transmissionContent = pushItem.content
        # template.title = pushItem.title
        # template.isRing = True
        # template.isVibrate = True
        # template.isClearable = True

        # message = IGtAppMessage()
        # message.data = template
        # message.isOffline = True
        # message.offlineExpireTime = 1000 * 3600 * 12

        # target = Target()
        # target.appId = self._APPID
        # target.clientId = self._CID
        # target.alias = self._CID

        # try:
        #     ret =self.pushService.pushMessageToSingle(message, target)
        #     print(ret)
        # except (Exception):
        #     print('error of push item %s' % pushItem)
        pass


from .mipush.APISender import APISender
from .mipush.base.APIMessage import *
from .mipush.APITools import *
from .mipush.APISubscribe import *
from .mipush.base.APIConstants import Constants


class MiPush():
    '''
    小米的推送服务
    '''

    _AppID = '2882303761517564997'
    _AppKey = '5761756432997'
    _AppSecret = 'ARnJ8qRQO1pypO8uxvw0TA=='
    _PackageName = 'push.jerry.cn.pushdispatcher'

    def __init__(self):
        self.sender = APISender(self._AppSecret)
    
    def sendTransmissionMessage(self, pushItem):
        '''
        发送一条透传消息
        '''
        pass

    def sendNotifycation(self, pushItem):
        """
        发送一个通知    参数为一条 消息实体
        """
        
        message = PushMessage() \
            .restricted_package_name('push.jerry.cn.pushdispatcher') \
            .title('这是一条测试消息') \
            .description('这是一条测试消息') \
            .pass_through(0) \
            .payload('payload') \
            .notify_type(1) \
            .extra({Constants.extra_param_notify_effect: Constants.notify_launcher_activity})
        recv = self.sender.send(message.message_dict(), 'jerry')
        print (recv)
        pass


def testMiPush(pushItem=None):
    if pushItem is None:
        raise Exception('push item can not be None')

    tools = APITools('ARnJ8qRQO1pypO8uxvw0TA==')

    # 查询消息状态
    #print(tools.query_message_status('msg_id').data)
    # 验证reg_id是否无效
    #print(tools.validate_reg_ids(['jerry']))
    # 获取无效reg_id
    #print(tools.query_invalid_reg_ids())
    # 获取无效alias
    #print(tools.query_invalid_aliases())
    # 获取设备设置alias
    #print(tools.query_device_aliases('push.jerry.cn.pushdispatcher', 'jerry'))

    mipushService = MiPush()
    mipushService.sendNotifycation(pushItem)
    print('ok')