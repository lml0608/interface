# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import sys
from src.common.MysqlHelper import MysqlHelper
import logging

logger = logging.getLogger(__name__)
print(logger)


datas = {
'sign_event':[
        {'id':1,'name':'红米Pro 发布会','`limit`':2000,'status':1,
        'address':'北京会展中心','start_time':'2017-08-20 14:00:00'},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,
        'address':'北京会展中心','start_time':'2017-08-20 14:00:00'},
        {'id':3,'name':'当前状态为0 关闭','`limit`':2000,'status':0,
        'address':'北京会展中心','start_time':'2017-08-20 14:00:00'},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,
        'address':'北京会展中心','start_time':'2001-08-20 14:00:00'},
        {'id':5,'name':'小米5 发布会','`limit`':2000,'status':1,
        'address':'北京国家会议中心','start_time':'2017-08-20 14:00:00'},
        ],
'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com',
        'sign':0,'event_id':1},
        {'id':2,'realname':'has ign','phone':13511001101,'email':'sign@mail.com',
        'sign':1,'event_id':1},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com',
        'sign':0,'event_id':5},
        ],

}

def init_data():

    # for table,data in datas.items():
    #     MysqlHelper.insert()

    #sql = "insert into sign_event values(1,'红米Pro发布会',2000,1,'北京会展中心','2017-08-20 14:00:00','2017-08-19 14:00:00')"
    #logger.info("你好")
    #MysqlHelper().insert(sql=sql,params=[])

    sql = "select id from ec_order_qrcode where product_group_id is not NULL and shelves_status=1"
    x = MysqlHelper().fetchall(sql,params=[])
    print(x)




init_data()