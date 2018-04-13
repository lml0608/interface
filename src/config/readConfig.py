# coding:utf-8
import os
import configparser
import codecs

cur_path = os.path.dirname(os.path.realpath(__file__))

print(cur_path)
configPath = os.path.join(cur_path, "cfg.ini")

print(configPath)
# #conf = ConfigParser.ConfigParser()
conf= configparser.ConfigParser()
#
conf.readfp(codecs.open(configPath, "r", "utf-8-sig"))
#
smtp_server = conf.get("email", "smtp_server")

print(smtp_server)

sender = conf.get("email", "sender")


psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")
