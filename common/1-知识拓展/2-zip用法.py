"""
======================
Author: 柠檬班-小简
Time: 2021/4/23 20:52
Project: day5
Company: 湖南零檬信息技术有限公司
======================
"""
a = ["class", "teacher", "student"]
b = ["py37", "xj", "many", "hello"]
c = [1, 2, 3]

res = dict(zip(a,b))
print(res)

res = list(zip(a,b,c))
print(res)