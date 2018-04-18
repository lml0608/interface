# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import unittest
import logging
import requests

class AddOrderTest(unittest.TestCase):
    '''下单限购'''

    def __init__(self,*args,**kwargs):

        super(AddOrderTest,self).__init__(*args,**kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):

        ''''''

        self.base_url = "http://test.wgmf.com/wechat-shop-back/order"

        #self.auth_user = ('admin','admin888')


    def test_add_order_guangdong_xiangou(self):
        '''龙岗 ID=8'''
        payload = {
            "addressId": 358,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 8,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url,json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'],10060)
        self.assertEqual(self.result['msg'],'广东省限购')

    def test_add_order_shenzhen_xiangou(self):
        '''龙岗 ID=6'''
        payload = {
            "addressId": 358,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 3,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 10060)
        self.assertEqual(self.result['msg'], '深圳市限购')

    def test_add_order_longgang_xiangou(self):
        '''龙岗 id=4'''
        payload = {
            "addressId": 358,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 210,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 10060)
        self.assertEqual(self.result['msg'], '龙岗区限购')

    def test_add_order_xiangou_luohu01(self):
        '''罗湖　iD=4'''
        payload = {
            "addressId": 366,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 210,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['msg'], '操作成功')

    def test_add_order_xiangou_luohu02(self):
        '''罗湖id=6'''
        payload = {
            "addressId": 366,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 3,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 10060)
        self.assertEqual(self.result['msg'], '深圳市限购')

    def test_add_order_xiangou_luohu03(self):
        '''a罗湖 ID=8'''
        payload = {
            "addressId": 366,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 8,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 10060)
        self.assertEqual(self.result['msg'], '广东省限购')

    def test_add_order_xiangou_guangdong01(self):
        '''广州其他地区 4'''
        payload = {
            "addressId": 359,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 210,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['msg'], '操作成功')

    def test_add_order_xiangou(self):
        '''广州其他地区 6'''
        payload = {
            "addressId": 359,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 3,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['msg'], '操作成功')

    def test_add_order_xiangou(self):
        '''广州其他地区 8'''
        payload = {
            "addressId": 359,
            "customerId": "16788112",
            "customerOpenId": "oxIF2juO_PiH7gZ-j1oRIHf6RU7w",
            "referrerOpenId": "",
            "buyerMemo": "",
            "orderDetails": [{
                "productId": 8,
                "quantity": 1
            }],
            "isPurchaseOrder": 0,
            "orderOrigin": 1,
            "isWebOrder": 1,
            "virtualMoney": 0
        }

        r = requests.post(self.base_url, json=payload)

        self.result = r.json()

        self.assertEqual(self.result['status'], 10060)
        self.assertEqual(self.result['msg'], '广东省限购')



    def tearDown(self):

        print(self.result)

