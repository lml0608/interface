# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest
import requests
import os
import sys
import logging


class AddEventTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AddEventTest, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

        print(self.logger)

    def setUp(self):

        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def test_add_event_all_null(self):
        self.logger.info("参数为空")

        payload = {'eid':'','':'','limit':'','address':"",'start_time':''}

        r = requests.post(self.base_url,data=payload)


        self.result = r.json()

        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_add_event_eid_exist(self):
        ''' id 已经存在'''

        payload = {'eid': 1, 'name': '一加4 发布会', 'limit': 2000,
                   'address': "深圳宝体", 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')


    def tearDown(self):
        self.logger.info("添加时间结束")

        print(self.result)
