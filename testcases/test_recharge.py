from lib2to3.pgen2 import token
import pytest
import os

from common.myConf import MyConf
from common.my_path import conf_dir
from common.my_requests import MyRequests

import pytest
import json
from common.My_excle import Myexcle
from common.my_requests import MyRequests
from common.my_assert import MyAssert
from common.mylogger import logger
from common.my_path import testdata_dir
from common.my_data import Data
from common.my_extract import extract_data_from_response
from common.my_replace import replace_case

#第一步，读取用户登录的测试数据，是个列表，列表中的每个成员，都是一个接口用例的数据
# excle_path = r"E:\Excle_test\test.xlsx"
excle_path = os.path.join(testdata_dir,"test.xlsx")
me = Myexcle(excle_path,"用户登录")
cases = me.read_data()

#第二步，遍历测试数据，每一组数据，发起http的接口
#实例化请求对象

mq = MyRequests()
massert = MyAssert()

# #初始化数据
# @pytest.fixture(scope="class")
# def prepare():
#     conf = MyConf(os.path.join(conf_dir,"data.ini"))
#     user = conf.get("normal","user")
#     passwd = conf.get("normal","passwd")
#     login_url = "api/v1/pub/login/3rd"
#     data = {"mobile_phone": user,"pwd": passwd}
#     resp = mq.send_requests("post",login_url,data)
#     #resp转换为字典
#     resp_list = resp.json()
#     member_id = resp_list["data"]["id"]
#     token = resp_list["data"]["token_info"]["token"]
#     leave_amount = resp_list["data"]["leave_amount"]

#     setattr(Data,"token",token)
#     setattr(Data,"member_id",str(member_id))
#     setattr(Data,"leave_amount",str(leave_amount))

    # yield token,member_id,leave_amount

# @pytest.mark.usefixtures("prepare")
class Recharge():
    @pytest.mark.parametrize("case",cases)
    #prepare是 yield的返回值
    def test_recharge(self,case):      #test_recharge(self,case,prepare)
    
        #1、下一个接口的请求数据中，需要替换为上一个接口中提取的数据,case为一行数据
        case = replace_case(case)
        # if case["req_data"] and case["req_data"].find("#member_id#") != -1:
        #     case["req_data"] = case["req_data"].replace("#member_id#",getattr(Data,"member_id"))
        
        # if case["assert_list"] and case["assert_list"].find("#leave_amount#") != -1:
        #     case["assert_list"] = case["assert_list"].replace("#leave_amount#",getattr(Data,"leave_amount"))
        
        # 2、把替换之后的请求数据（json格式的字符串）。转换成一个字典
        req_dict = json.loads(case["req_data"])

        #3、发送一个请求，并接收响应结果
        if hasattr(Data,"token"):
            resp = mq.send_requests(case["url"],case["method"],req_dict,token=getattr(Data,"token"))
        else:
            resp = mq.send_requests(case["url"],case["method"],req_dict)
        logger.info(resp.json())
        #4、提取结果中的响应数据--代替前面的前置处理
        if case["extract"]:
            #调用提取处理函数
            extract_data_from_response(case["extract"],resp.json())

        #结果空列表
        assert_res = []
        #5、断言响应结果--响应结果断言成功之后再提取-第四步
        if case["assert_list"]:
            logger.info("提取出来的测试数据为：{}".format(case["assert_list"]))
            response_check_res = massert.assert_response_value(case["assert_list"],resp.json())

            # logger.info("断言的结果为：{}".format(response_check_res))
            assert_res.append(response_check_res)
            logger.info("断言结果为：{}".format(assert_res))

      

        #6、断言数据库
        # if case["assert_db"]:
        #     db_check_res = massert.assert_db(case["assert_db"],resp.json())
        #     assert_res.append(db_check_res)
          
        #最终的AssertionError异常
        if False in assert_res:
            raise AssertionError
        
        #从响应结果中，提取leave_amount的值，并更新全局变量中，leave_amount的值
        setattr(Data,"leave_amount",str(resp.json()["data"]["leave_amount"]))

    