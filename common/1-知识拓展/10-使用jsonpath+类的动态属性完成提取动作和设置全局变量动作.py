"""
======================
Author: 柠檬班-小简
Time: 2021/5/8 21:21
Project: day10
Company: 湖南零檬信息技术有限公司
======================
"""
"""
从响应结果当中，提取值，并设置为全局变量(Data类作为本框架的全局变量类)
1、提取表达式：放在excel当中
   (可能提取1个，可能提取多个。。以表达式个数为准)

2、提取出来之后，设置为Data类属性
"""
import jsonpath
from common.my_data import Data
# 测试数据
extract_epr = '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
response = {"code":0,"msg":"OK","data":{"id":16,"leave_amount":876203.87,"mobile_phone":"15500000000","reg_name":"小柠檬","reg_time":"2021-01-28 15:19:50.0","type":1,"token_info":{"token_type":"Bearer","expires_in":"2021-05-08 20:54:58","token":"eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjE2LCJleHAiOjE2MjA0Nzg0OTh9.ab1jN6Bm4KOCnmhMyAPOOV0RNfn-d7xcJERsAWL8KpYNy0lPL5YQGYvuKQGzIbwPWHthj1v_xXKMueImAtqZcQ"}},"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}

# 1、从excel中读取的提取表达式，转成字典对象
extract_dict = eval(extract_epr)

# 2、遍历1中字典的key,value.key是全局变量名，value是jsonpath表达式。
for key,value in extract_dict.items():
    # 根据jsonpath从响应结果当中，提取真正的值。value就是jsonpath表达式
    result = jsonpath.jsonpath(response, value)
    # jsonpath找了就是列表，找不到返回False
    # 如果提取到了真正的值，那么将它设置为Data类的属性。key是全局变量名，result[0]就是提取后的值
    if result:
        setattr(Data, key, result[0])

print("======================================")
# 打印一下Data类的属性
for key,value in Data.__dict__.items():
    print(key, value)