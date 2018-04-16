# coding:utf-8
import os
import configparser
import codecs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

configPath = os.path.join(BASE_DIR, "cfg.ini")


cf = configparser.ConfigParser()
cf.read(configPath, encoding='utf-8')



#cf.read(codecs.open(configPath, "r", "utf-8-sig"))

###############邮箱信息#####################
smtp_server = cf.get("email", "smtp_server")

sender = cf.get("email", "sender")

psw = cf.get("email", "psw")

receiver = cf.get("email", "receiver")

port = cf.get("email", "port")

###############MySQL###################

host = cf.get("mysql",'host')
port = cf.get("mysql",'port')
user = cf.get("mysql",'user')
password = cf.get("mysql",'password')
db_name = cf.get("mysql",'db_name')

