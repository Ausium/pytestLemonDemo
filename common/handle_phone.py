
import os
import sys

from numpy import true_divide
sys.path.append(os.getcwd())

from hashlib import new
from faker import Faker
from common.my_mysql import MyMysql


def get_new_phone():
    """
    # 得到没有注册过的手机号码。
    # 1、使用faker生成手机号码
    # 2、调用mysql数据库操作，去判断是否在数据中存在。如果不在，表示没有注册
    :return:
    """
    while True:
        phone = Faker("zh_CN").phone_number()
        sql = "select id from member where mobile_phone='{}'".format(phone)
        res = MyMysql().get_count(sql)
        if res == 0:
            return phone

def is_exist_phone(phone_num):
    """
    # 得到没有注册过的手机号码。
    # 1、使用faker生成手机号码
    # 2、调用mysql数据库操作，去判断是否在数据中存在。如果不在，表示没有注册
    :return:
    """
    sql = "select id from member where mobile_phone='{}'".format(phone_num)
    res = MyMysql().get_count(sql)
    if res == 0:
        return False
    else:
        return True
   

if __name__ == "__main__":
    new_phone = get_new_phone()
    print(new_phone)

