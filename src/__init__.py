# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import logging
import logging.config
import logging.handlers
import time

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
filepath = os.path.join(BASE_DIR,'config/logging.conf')

# print(filepath)


logging.config.fileConfig(filepath) # disable_existing_loggers=0

# logger = logging.getLogger(__name__)



# print(logger)


#logging.getLogger("selenium").setLevel(logging.WARNING)

# curtime = time.strftime("%Y%m%d%H%M%S",time.localtime())
#
# #handler = logging.handlers.TimedRotatingFileHandler(logFile)
#
# fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-8s: %(message)s'
#
# formatter = logging.Formatter(fmt)
#
#
# logFile = os.path.abspath(os.path.join(os.getcwd(),'logs','log_{}'.format(curtime)))
# handler = logging.handlers.RotatingFileHandler(logFile,maxBytes=4096000000,backupCount=9)
# handler.setFormatter(formatter)
# logger.addHandler(handler)

