#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Created on 2016-12-09   上午10:48

@project: pushSystem
@author: JieGuo
"""

__author__ = 'JieGuo'

import os, json
import requests

class Api():

    _BASE_URl = 'http://139.196.228.153:8086/api'

    _authorization = 'unset'
    _header = {
        'Accept-Charset'    : 'utf-8',
        'Content-Type'      : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection'        : 'keep-alive',
        'Accept'            : '*/*',
        'x-version'         : '2.2.6',
        'x-platform'        : 'android',
        'x-client'          : 'store',
    }

    def __init__(self, debug=False):
        self._debug=debug

    def _getHeader(self, authorization, isLogin=False):

        if authorization and isLogin :
            self._header['Authorization'] = authorization
        elif authorization :
            self._header['Authorization'] = 'Bearer %s' % authorization

        
        return self._header

    def login(self, username, password):
        data = {
            'equType' : 1,
            'grant_type' : 'password',
            'scope' : 'read',
            'username' : username,
            'password' : password
        }
        response = self.post('/oauth/token', data)
        result = response.text
        if result :
            responseJson = json.loads(result)
            self._authorization = responseJson['result']['access_token']
            print(self._authorization)
            return True
        return False

    def auth(self):
        pass

    def checkLogin(self):
        pass

    def get(self, path):
        url = '%s%s' % (self._BASE_URl, path)
        header = self._getHeader('Basic Zm9vOmJhcg==', True)
        data = {
            'equType' : 1,
            'grant_type' : 'password',
            'scope' : 'read',
            'username' : '13365601544',
            'password' : 'tt123456'
        }
        response = requests.get(url, data, headers=header)
        print(response.status_code)
        print(response.text)

    def post(self, path, data):
        url = '%s%s' % (self._BASE_URl, path)
        header = self._getHeader('Basic Zm9vOmJhcg==', True)
        
        response = requests.post(url, data=data, headers=header)
        if self._debug : 
            print('request url : ', url)
            print('header : ', header)
            print(response.status_code)
            print(response.text)

        if response.status_code == 200:
            return response
        elif response.status_code == 500 or response.status_code == 404:
            raise Exception('post error status code is : %s' % response.status_code)
        return response

if __name__ == '__main__':
    api = Api(debug=True)
    api.login('13365601544', 'tt123456')