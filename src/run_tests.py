# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


import time
import sys
import os
import unittest
from HTMLTestRunner import HTMLTestRunner



test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'interface')

print(test_dir)

discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

print(discover)


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()