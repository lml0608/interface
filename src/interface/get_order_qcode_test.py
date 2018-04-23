# -*- coding:utf-8 -*-
'''
__author__:liubin 

'''
import unittest
import logging
import requests

class GetQcodeTest(unittest.TestCase):
    '''发布会查询接口'''

    def __init__(self,*args,**kwargs):

        super(GetQcodeTest,self).__init__(*args,**kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):

        ''''''

        self.base_url = "http://test.wgmf.com/wechat-shop-back/product/getQRCodeUrl/00532/0110074"



    def test_get_qcode_success(self):
        '''auth为空'''

        self.logger.info('请求二维码数据')
        r = requests.get(self.base_url)
        num = 0
        self.result = r.json()
        for mylist in self.result['data']['purchaseYesResultList'] + self.result['data']['purchaseNoResultList']:

            num += len(mylist['qrCodeInfo'])
        #
        # for nolist in self.result['data']['purchaseNoResultList']:
        #
        #     num += len(nolist['qrCodeInfo'])

        print(num)

        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['msg'],'操作成功')
        self.assertEqual(num,16)




    def tearDown(self):

        #print(self.result)
        pass

