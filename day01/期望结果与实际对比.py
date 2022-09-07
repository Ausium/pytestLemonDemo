import os
import sys
sys.path.append(os.getcwd())

import ast
from tabnanny import check
from urllib import response
from common.My_excle import Myexcle
import jsonpath

check_str = '[{"expr":"$.code","expected":"0","type":"eq"}]'

{'Status': 400, 'Message': '无效的用户名或密码'}


response = {
    "code":0,
    "msg":"OK",
    "data":{
        "id":"10086",
        "reg_name":"小欧",
        "mobile_phone":"13398080008"
    }
}

#把字符串转换成python列表

check_list = ast.literal_eval(check_str)

print(check_list[0]["expected"])
# print(check_list)

#对比结果列表
check_res = []

for check in check_list :
    #jsonpath.jsonpath   这个是返回一个列表
    actual = jsonpath.jsonpath(response,check["expr"])
    print(actual[0])
    if isinstance(actual,list):
        actual = actual[0]
    #与实际结果做比对
    if check["type"] == "eq":
        check_res.append(actual == check["expected"])
    
print(check_res)

if False in check_res:
    AssertionError 





