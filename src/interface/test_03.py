# coding:utf-8
import unittest
import requests
from interface import Blog

import logging

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)


    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_login(self):
        u'''测试登录用例'''
        self.logger.info("------start!--------")
        result = self.blog.login()
        self.logger.info(u"调用登录结果：%s"%result)
        self.logger.info(u"获取是否登录成功：%s"%result["success"] )
        self.assertEqual(result["success"] , True)    # 拿结果断言
        self.logger.info("------end!--------")

    def test_del(self):
        u'''测试保存草稿箱-删除用例'''
        self.logger.info("------start!--------")
        # 第一步：登录
        self.logger.info(u"第一步：登录")
        self.blog.login()
        # 第二步：保存
        self.logger.info(u"第二步：保存")
        r2_url = self.blog.save("wQEW12", "WQASDA21e3S")
        pid = self.blog.get_postid(r2_url)
        # 第三步：删除
        self.logger.info(u"第三步：删除")
        result = self.blog.del_tie(pid)
        self.assertEqual(result["isSuccess"], True)
        self.logger.info("------end!--------")

if __name__ == "__main__":
   unittest.main()
