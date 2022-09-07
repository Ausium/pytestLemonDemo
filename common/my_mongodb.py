from gc import collect
from typing import Collection
from unittest import result
import pymongo

def find():
    # hots：mongodb服务器ip
    # port：端口，默认为27017
    # user：账号  【可选项】
    # pwd：密码 【可选项】
    client = pymongo.MongoClient( 
                                host='10.10.10.16',
                                port=27017,
                                username='admin',
                                password='root123' 
                                )

    db = client.platform_admin  # mydb为数据库

    # # 库中的集合 mycol 有以下两种方式调用，col_name 为集合名字
    # mycol = db['car_info']
    # mycol = db.car_info
    collection = db.car_info
    result = collection.find({"car_info_id" : "adv-gt-53"})
    print(result)
    for doc in result:
        if doc["car_info_id"]:
            print(doc["car_info_id"])
        else:
            print("none")
	    # print(doc)
    # 关闭
    client.close()

find()

