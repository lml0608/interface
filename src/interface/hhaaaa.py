# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import logging
import unittest

class telogggtLogin(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(telogggtLogin, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)


        print(self.logger)

    def setUp(self):
        pass


    def test_001(self):

        self.logger.warning("nihao")

    def tearDown(self):
        print('wfw')




