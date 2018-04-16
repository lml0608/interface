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


    def tearDown(self):
        self.logger.info("添加时间结束")

        print(self.result)
