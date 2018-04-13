# coding:utf-8
import unittest
import requests
import logging
class Test_Kuaidi(unittest.TestCase):
    u'''测试快递查询接口'''

    def __init__(self, *args, **kwargs):
        super(Test_Kuaidi, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        print(self.logger)

    def setUp(self):

        self.logger.info("nihao")
        self.headers = {
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
                  }  # get方法其它加个ser-Agent就可以了

    def chaxun_kuaidi(self, danhao, kd, kd_name):
        '''三个参数：单号、快递名称（拼音）、快递中文名
        如：
        danhao = '1202247993797'
        kd = 'yunda'
        kd_name = u"韵达快递"
        '''
        # 这里对url的单号参数了
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao, kd)
        self.logger.info(u"测试url地址：%s"%self.url)
        # 第一步发请求
        r = requests.get(self.url, headers=self.headers, verify=False)
        result = r.json()
        self.logger.info(u"获取请求结果：%s"%result)
        # 第二步获取结果
        self.logger.info(u"获取公司名称：%s"%result['company'])
        data = result["data"]   # 获取data里面内容
        self.logger.info(u"获取data内容：%s"%result["data"])
        get_result = data[0]['context']  # 获取已签收状态
        self.logger.info(u"获取已签收状态：%s"%get_result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(kd_name, result['company'])
        self.assertIn(u"已签收", get_result)


    def test_yunda(self):
        u'''测试韵达快递，单号：1202247993797'''
        self.logger.info("----------start!-------")
        danhao = '1202247993797'
        kd = 'yunda'
        kd_name = u"韵达快递"
        self.logger.info(u"测试单号：%s  快递名称：%s"%(danhao, kd_name))
        self.chaxun_kuaidi(danhao, kd, kd_name)
        self.logger.info("----------pass!-------")

    def test_tiantian(self):
        u'''测试天天快递，单号：560697415000'''
        self.logger.info("----------start!-------")
        danhao = '560697415000'
        kd = 'tiantian'
        kd_name =u"天天快递"
        self.logger.info(u"测试单号：%s  快递名称：%s"%(danhao, kd_name))
        self.chaxun_kuaidi(danhao, kd, kd_name)
        self.logger.info("----------pass!-------")
if __name__ == "__main__":
    unittest.main()