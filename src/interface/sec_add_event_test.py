# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest
import requests
import logging
import base64, time
import hashlib

class AddEventTest(unittest.TestCase):

    '''数字签名添加发布会'''

    def __init__(self, *args, **kwargs):
        super(AddEventTest, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
    def setUp(self):

        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        self.api_key = "&Guest-Bugmaster"
        now_time = time.time()

        self.client_time = str(now_time).split('.')[0]
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key

        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")

        md5.update(sign_bytes_utf8)

        self.sign_md5 = md5.hexdigest()


    def test_add_event_sign_null(self):
        '''参数为空'''
        payload = {'eid':1,'name':'','limit':'','address':"",'start_time':'','time':'','sign':''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.logger.info("获得结果")
        self.assertEqual(self.result['status'],10012)
        self.assertEqual(self.result['message'],'user sign null')


    def test_add_event_time_out(self):
        '''请求超时'''
        now_time = str(int(self.client_time) - 61)

        payload = {'eid': 1, 'name': '一加4 发布会', 'limit': 2000,
                   'address': "深圳宝体", 'start_time': '2017','time':now_time,'sign':'abc'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10013)
        self.assertEqual(self.result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        ''' 名称已经存在'''

        payload = {'eid': 10, 'name': '红米Pro发布会', 'limit': 2000,
                   'address': "北京水立方", 'start_time': '2017','time':self.client_time,'sign':'abc'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10014)
        self.assertEqual(self.result['message'], 'user sign error')



    def test_add_event_success(self):
        ''' 添加成功'''

        payload = {'eid': 12, 'name': '一加4 手机发布会2', 'limit': 2000,
                   'address': "北京水立方", 'start_time': '2017-05-10 12:00:00','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


    def tearDown(self):

        print(self.result)
