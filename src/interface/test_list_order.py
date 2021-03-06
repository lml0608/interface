# coding:utf-8
import unittest
import requests
import logging
# 禁用安全请求警告
# from requests.packages.urllib3.exceptions import
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class test_order(unittest.TestCase):
    #logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        super(test_order, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

        print(self.logger)


    def setUp(self):
        self.headers = {
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
                  }  # get方法其它加个ser-Agent就可以了


    def test_order_list(self):
        '''三个参数：
        账号：username，密码：psw,记住登录：reme=True'''
        url = "http://test.wgmf.com/wechat-shop-back/order/list?cusId=16788112&openId=&curPage=1&pageSize=10"

        r = requests.get(url, headers=self.headers, verify=False)


        self.result = r.json()  # 字节输出
        self.logger.info("你好")

        print(type(self.result)) #dict
        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['msg'], '操作成功')
        self.assertEqual(len(self.result['data']), 10)


        print(self.result['data'][0]['orderCode'])

    def tearDown(self):

        self.logger.info("结束")










if __name__ == "__main__":
    unittest.main()


