"""
======================
Author: 柠檬班-小简
Time: 2021/5/8 20:36
Project: day10
Company: 湖南零檬信息技术有限公司
======================
"""
"""

setattr(对象/类, attr, value)
getattr(对象/类, attr)
hasattr(对象/类, attr) True表示有attr, False表示没有attr
delattr(对象/类, attr)

在代码运行的过程中，动态的给Data类设置/获取/删除属性。
"""
class Data:
    pass

setattr(Data, "token", "1234564562314584555")

if hasattr(Data, "token"):
    value = getattr(Data,"token")
    print(value)
    # delattr(Data, "token")