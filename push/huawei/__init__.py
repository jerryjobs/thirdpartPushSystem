#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'

import os
import requests
import json, time
from urllib.parse import quote_plus


class HuaWeiPush():
    '''
    华为push service 
    '''

    _APPID = '100065355'
    _APPSECRET = '51ecf881300a0a78397c9ca7baf332e5'
    _TOKEN = ''
    _EXPIRES_IN = 0

    def __init__(self):
        if self._TOKEN == '' and self.auth() :
            print(self._TOKEN)
        else :
            print('sorry auth fail')

    def auth(self):
        response = requests.post('https://login.vmall.com/oauth2/token', data={
            'grant_type' : 'client_credentials',
            'client_secret' : self._APPSECRET,
            'client_id' : self._APPID
        }, headers={
            'Content-Type' : 'application/x-www-form-urlencoded'
        })

        if response.status_code == 200:
            
            respJson = json.loads(response.text)
            print(respJson)
            if respJson['access_token'] :
                self._TOKEN = respJson['access_token']
                self._EXPIRES_IN = respJson['expires_in']
                return True
        else:
            raise Exception('auth huawei get token error')

        return False

    def send_push(self, pushItem):

        if self._TOKEN == '' :
            raise Exception('no token error')
        
        if pushItem is None or pushItem.target is None or pushItem.target == '':
            raise Exception('Push item can not be None')

        token = quote_plus(self._TOKEN)
        target = quote_plus('["%s"]' % pushItem.target)

        payloadStr = '{"hps":{"msg":{"type":"%s","body":{"content":"%s","title":"%s"}}}}' % (3, pushItem.title, pushItem.content)

        url = 'https://api.push.hicloud.com/pushsend.do?access_token=%s&nsp_svc=%s&nsp_ts=%s&device_token_list=%s&payload=%s&nsp_ctx=%s' % \
        (token, 'openpush.message.api.send', int(time.time()), target, quote_plus(payloadStr), '%7b%22ver%22%3a%221%22%2c+%22appId%22%3a%2210923253325%22%7d')


        response = requests.post(url, data={}, headers={
            'Content-Type' : 'application/x-www-form-urlencoded'
        })

        if response.status_code == 200 :
            print(response.text)
        else :
            print('push error', response.text)

class HueaweiPushMessage() :
    '''
    # PUSH消息类型  Payload
    { 
        "hps": {                                        
            "msg" : {                                        
                "type" : 1,                                        
                "body" : {"key":"value"}                                        
            }                                        
        }  
    }    

    # 系统通知栏异步消息                
    {                            
        "hps": {                                         
             "msg" : {                                        
                "type" : 3,                                        
                "body" : {                                        
                    "content" : "Push message content", 
                    "title" : "Push message content"                            
                 },                                         
                "action" : {                                        
                    "type" : 1,                                        
                    "param" : {                                        
                        "intent":"#Intent;compo=com.rvr/.Activity;S.W=U;end"                            
                    }                                        
                }                                        
        },                                        
        "ext" : {                                        
            "biTag" : "Trump",                                        
            "icon" : "http://upload.w.org/00/150pxsvg.png"                            
        }                                        
    }    

    # 扩展消息   
      {                            
        "hps": {                                         
                "msg" : {                                        
                    "type" : 3,                                        
                    "body" : {                                        
                            "content" : "Push message content", 
                            "title" : "Push message content"                            
                    },                                         
                    "action" : {                                        
                            "type" : 1,                                        
                            "param" : {                                        
                                "intent":"#Intent;compo=push.jerry.cn.pushdispatcher/.MainActivity;S.W=U;end"                            
                            }                                        
                    }                                        
            },                                        
            "ext" : {                                        
                    "biTag" : "Trump",                                        
                    "customize" :[{"season":"Spring"},{"weather":"raining"}]                            
            }                                        
        }                                                                
    '''
    _hps = ''

    def __init__(self):
        pass



if __name__ == '__main__' :
    print('hi this is the test')
    push = HuaWeiPush()
    push.send_push_test()