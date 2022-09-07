
from asyncio.log import logger
from cgi import print_arguments
import json
import os
import sys
sys.path.append(os.getcwd())
# """
# 从响应结果当中，提取值，并设置为全局变量(Data类作为本框架的全局变量类)
# 1、提取表达式：放在excel当中
#    (可能提取1个，可能提取多个。。以表达式个数为准)
#
# 2、提取出来之后，设置为Data类属性
# """
import jsonpath
import os
from common.my_data import Data
from common.my_path import testdata_dir
from common.My_excle import Myexcle
from common.mylogger import MyLogger

def extract_data_from_response(extract_epr, response_dict):
    """
    从响应结果当中提取值，并设置为Data类的属性。
    :param extract_epr: excel当中extract列中的提取表达式。是一个字典形式的字符串。
                        key为全局变量名。value为jsonpath提取表达式。
                        '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
    :param response: http请求之后的响应结果。字典类型。
    :return:None
    """
    # 1、从excel中读取的提取表达式，转成字典对象
    extract_dict = eval(extract_epr)
    # print(extract_dict)
    # 2、遍历1中字典的key,value.key是全局变量名，value是jsonpath表达式。
    for key,value in extract_dict.items():
        # 根据jsonpath从响应结果当中，提取真正的值。value就是jsonpath表达式
        logger.info("提取的变量名为：{}，提取到的jsonpath表达式为：{}".format(key,value))
        result = jsonpath.jsonpath(response_dict, value)
        logger.info("jsonpath提取之后的值为{}".format(result))
        # jsonpath找了就是列表，找不到返回False
        # 如果提取到了真正的值，那么将它设置为Data类的属性。key是全局变量名，result[0]就是提取后的值
        if result:
            setattr(Data, key, str(result[0]))
            logger.info("提取的变量名为：{}，提取到的值为：{},并设置为Data类的属性和值。".format(key,str(result[0])))

if __name__ == '__main__':
    cases = '{"token":"$..token","member_id":"$..member_id","leave_amount":"$..leave_amount"}'
    case = eval(cases)
    print(case)
    for key,value in case.items():
        print(key,value)

   



