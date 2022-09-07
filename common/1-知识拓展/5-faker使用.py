"""
======================
Author: 柠檬班-小简
Time: 2021/4/26 21:54
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
"""
faker造数据：
faker的官方文档：https://faker.readthedocs.io/en/master/locales.html
测试派文章：http://testingpai.com/article/1615615023407

1、安装：
pip install faker

2、使用:
   1) 导入：from faker import Faker
   2) 语言支持：
        简体中文：zh_CN
        繁体中文：zh_TW
        美国英文：en_US
        英国英文：en_GB
        德文：de_DE
        日文：ja_JP
        韩文：ko_KR
        法文：fr_FR
        比如中文：f = Faker("zh_CN")

   3) faker提供的数据生成类型：
       faker.Provider

示例：
f = Faker("zh_CN")
print(f.phone_number())

支持自己定义数据生成规则 ：
Faker 已经提供了足够丰富的信息生成，包括名字、手机号、邮箱地址、邮编等等。尽管如此，可能还是没有办法满足你的需求。

这时，可以利用自定义扩展，引用外部的 provider，自定义你要的功能。

Faker 对象可以通过 add_provider 方法将自定义的 Provider 添加到对象中,自定义的 Provider 需要继承自 BaseProvider。



"""
from faker import Faker

f = Faker("zh_CN")
print(f.phone_number())
