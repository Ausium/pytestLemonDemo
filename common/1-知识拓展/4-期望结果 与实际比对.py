"""
======================
Author: 柠檬班-小简
Time: 2021/4/26 20:39
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
import ast

# 从excel当中，读取出来的断言列表
check_str = '[{"expr":"$.code","expected":0,"type":"eq"},{"expr":"$.msg","expected":"OK","type":"eq"}]'

# 把字符串转换成python列表
check_list = ast.literal_eval(check_str)  # 比eval安全一点。转成列表。
print(check_list)

# 响应结果
response = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 1000396245,
        "reg_name": "小柠檬",
        "mobile_phone": "13300003488"
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}

# 如何从响应果当中，通过jsonpath表达式，提取出要比对的数据。
# 第三方库：jsonpath
import jsonpath

# 比对结果列表
check_res = []

for check in check_list:
    # 通过jsonpath表达式，从响应结果当中拿到了实际结果
    actual = jsonpath.jsonpath(response, check["expr"])
    if isinstance(actual,list):
        actual = actual[0]
    # 与实际结果做比对
    if check["type"] == "eq":
        check_res.append(actual == check["expected"])

if False in check_res:
    AssertionError



