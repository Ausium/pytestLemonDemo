
import os
import sys
sys.path.append(os.getcwd())

import pytest
import json
from common.handle_phone import get_new_phone
from common.My_excle import Myexcle
from common.my_requests import MyRequests
from common.my_assert import MyAssert
from common.mylogger import logger
from common.my_path import testdata_dir
from common.my_replace import replace_case


#第一步，读取用户登录的测试数据，是个列表，列表中的每个成员，都是一个接口用例的数据 BA-110PL-7A1
# excle_path = r"E:\Excle_test\test.xlsx"
# excle_path = os.path.join(testdata_dir,"test.xlsx")
excle_path = testdata_dir()
me = Myexcle(excle_path,"用户登录")
cases = me.read_data()

#第二步，遍历测试数据，每一组数据，发起http的接口
#实例化请求对象

mq = MyRequests()
massert = MyAssert()
class TestLogin :
    
    #参数名case是用来接收每一组的数据，并作为测试用例的参数
    @pytest.mark.parametrize("case",cases)
    def test_login(self,case):
        
        logger.info("开始登录")

        #替换掉占位符 - 请求数据和断言里面替换掉#phone#，替换成未注册手机号码,-1是表示有数据返回
        #1、如果有需要替换的占位符就要替换
        case = replace_case(case)
        
        """
        因为现在的case["req_data"]还是一个json格式的字符串，所以需要转化成一个字典
        2、把替换之后的请求数据（json格式的字符串）。转换成一个字典
        json.loads无法转换单引号数据(单引号非json格式)
        eval 则无视单引号 双引号
        """
        logger.info("--------------req_data提取的操作值为：\n{}".format(case["req_data"]))
        logger.info('---case["req_data"]的数据类型为\n{}'.format(type(case["req_data"])))
        
        req_dict = json.loads(case["req_data"])  
        logger.info("req_dict的数据为：{}".format(req_dict))
        logger.info("--------------req_dict提取的操作值为：{}".format(req_dict))
        logger.info("req_dict的数据类型为{}".format(type(req_dict)))

        #3、发送一个请求，并接收响应结果
        resp = mq.send_requests(case["url"],case["method"],req_dict)
        # print(resp.json())
        #结果空列表
        assert_res = []
        #4、断言响应结果
        if case["assert_list"]:
            logger.info("提取出来的测试数据为：{}".format(case["assert_list"]))
            response_check_res = massert.assert_response_value(case["assert_list"],resp.json())
            logger.info("响应结果为：{}".format(resp.json()))
            # logger.info("断言的结果为：{}".format(response_check_res))
            assert_res.append(response_check_res)
            logger.info("断言结果为：{}".format(assert_res))

        #5、断言数据库
        # if case["assert_db"]:
        #     db_check_res = massert.assert_db(case["assert_db"],resp.json())
        #     assert_res.append(db_check_res)
          
        #最终的AssertionError异常
        if False in assert_res:
            raise AssertionError

if __name__ == '__main__':
    excle_path = os.path.join(testdata_dir,"test.xlsx")
    me = Myexcle(excle_path,"用户登录")
    cases = me.read_data()
    print(cases)
    