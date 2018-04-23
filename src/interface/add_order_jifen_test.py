# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import unittest
import logging
import requests

class AddOrderJifenTest(unittest.TestCase):
    '''下单限购'''

    def __init__(self,*args,**kwargs):

        super(AddOrderJifenTest,self).__init__(*args,**kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):

        ''''''

        self.base_url = "http://test.wgmf.com/wechat-shop-back/order"

        #self.auth_user = ('admin','admin888')


    def test_add_order_use_jifen(self):
        '''testjifen'''
        json_data = {
            "addressId": 324,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": '',
            "buyerMemo": "测试单不发货",
            "orderDetails": [{
                "productId": 211,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 0,
            "isWebOrder": 1,
            "virtualMoney": -0.01
        }

        r = requests.post(self.base_url,json=json_data)

        self.result = r.json()

        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['msg'],'积分不足')

    def tearDown(self):

        print(self.result)