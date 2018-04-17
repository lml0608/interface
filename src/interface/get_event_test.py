# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import unittest
import logging
import requests

class GetEventListTest(unittest.TestCase):
    '''发布会查询接口'''

    def __init__(self,*args,**kwargs):

        super(GetEventListTest,self).__init__(*args,**kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):

        ''''''

        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"

        self.auth_user = ('admin','admin888')


    def test_get_event_list_auth_null(self):
        '''auth为空'''

        r = requests.get(self.base_url,params={'eid':''})

        self.result = r.json()

        self.assertEqual(self.result['status'],10011)
        self.assertEqual(self.result['message'],'user auth null')


    def test_get_event_list_auth_error(self):
        '''auth错误'''

        r = requests.get(self.base_url,auth=('abc','123'),params={'eid':''})

        self.result = r.json()

        self.assertEqual(self.result['status'],10012)
        self.assertEqual(self.result['message'],'user auth fail')



    def test_get_event_list_eid_null(self):
        '''ID为空'''

        r = requests.get(self.base_url,auth=self.auth_user,params={'eid':''})

        self.result = r.json()

        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')



    def test_get_event_list_eid_success(self):
        '''查询成功'''
        r = requests.get(self.base_url,auth=self.auth_user,params={'eid':1})

        self.result = r.json()

        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')

    def tearDown(self):

        print(self.result)

