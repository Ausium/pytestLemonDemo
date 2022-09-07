"""
======================
Author: 柠檬班-小简
Time: 2021/5/7 21:36
Project: day9
Company: 湖南零檬信息技术有限公司
======================
"""
import ast
import json


# strr = '{"expected":2500+2000}'
#
# res = eval(strr)
# print(res)

# ress = ast.literal_eval(strr)
# print(ress)

# # json串和python对象的转换。
# ress = json.loads(strr)
# print(ress)

strr = """
[{"expr":"$.code","expected":0,"type":"eq"},
{"expr":"$.msg","expected":"OK","type":"eq"},
{"expr":"$..leave_amount","expected":2000.55+2000,"type":"eq"}
]
"""

res = eval(strr)
print(res)