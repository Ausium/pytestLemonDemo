"""
======================
Author: 柠檬班-小简
Time: 2021/5/8 21:42
Project: day10
Company: 湖南零檬信息技术有限公司
======================
"""
ss = '{"member_id":#member_id#,"amount":2000}'
member_id = "16"
new_ss = ss.replace("#member_id#", member_id)
print(new_ss)
