# -*- coding:utf-8 -*-
'''
__author__:liubin 

'''
import unittest
import logging
import requests

class GetNoticeTest(unittest.TestCase):
    '''发布会查询接口'''

    def __init__(self,*args,**kwargs):

        super(GetNoticeTest,self).__init__(*args,**kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):

        ''''''

        self.base_url = "http://test.wgmf.com/wechat-shop-back/product/info/notice"



    def test_get_notice_success(self):
        '''auth为空'''

        self.logger.info('请求公告信息')
        r = requests.get(self.base_url)

        self.result = r.json()

        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['msg'],'操作成功')
        self.assertEqual(len(self.result['data']),0)


    # def test_get_event_list_auth_error(self):
    #     '''auth错误'''
    #
    #     r = requests.get(self.base_url,auth=('abc','123'),params={'eid':''})
    #
    #     self.result = r.json()
    #
    #     self.assertEqual(self.result['status'],10012)
    #     self.assertEqual(self.result['message'],'user auth fail')







    def tearDown(self):

        print(self.result)

