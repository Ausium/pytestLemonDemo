from asyncio.log import logger
from multiprocessing.spawn import import_main_path
import pytest
from common.my_data import Data
from common.handle_phone import is_exist_phone
from common.my_requests import MyRequests


@pytest.fixture(scope="session",autouse=True)
def global_init():
    """
    配置全局的用户信息，要确保一定是存在的
    1、从Data里拿出来用户数据
    2、调用sql从数据库查询，如果不存在则注册
    """
    for user in Data.global_user:
        res = is_exist_phone(user)
        if not res: 
            logger.info("全局使用账号{}不存在，现在注册一个用户".format(user))
            #调用注册方法
            req_data = {"mobile_phone": "user","pwd": "123456789"}
            res = MyRequests.send_requests("post","http://member/register",req_data)
            logger.info("注册结果为：{}".format(res.text))
            