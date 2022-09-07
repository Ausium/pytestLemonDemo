
from asyncio.log import logger
import re
from common.my_data import Data
from common.mylogger import MyLogger
from common.handle_phone import get_new_phone

"""
替换测试用例中所有的标识符，通过正则表达式获取所有的mark，然后遍历mark一个个替换，
替换的值来自于：
1、如果是#phone#，则来自于脚本生成
2、其他的mark。均从Data类属性中获取

在测试框架中，Data类中主要用在什么地方？
1、法封装的提取方法(从响应结果中提取数据放到Data中)
2、封装的替换方
"""


def replace_case(case_dict):
    # 第一步，把excel当中的一整个测试用例(excel当中的一行)转换成字符串
    case_str = str(case_dict)
    # print(case_str)

    # 第二步，利用正则表达式提取mark标识符
    to_be_replace_marks_list = re.findall("#(\w+)#",case_str)
    

    # 第三步：遍历标识符mark，如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
    if to_be_replace_marks_list:
        logger.info("要替换的标识符为：".format(to_be_replace_marks_list))

        #判断是否有phone这个标识符，如果有，调用生成手机号码的脚本，然后替换
        if "#phone#" in to_be_replace_marks_list:
            new_phone = get_new_phone()
            logger.info("有#phone#标识符，需要生成的手机号码为：{}".format(new_phone))
            case_str = case_str.replace(f"#phone#",new_phone)

        for mark in to_be_replace_marks_list:
            # 如果全局变量Data类有mark这个属性名
            if hasattr(Data, mark):
                logger.info("将标识符{}替换为{}".format(mark,getattr(Data,mark)))
                # 使用全局变量Data类的mark属性值，去替换测试用例当中的#mark#
                case_str = case_str.replace(f"#{mark}#", getattr(Data,mark))
        
        
        logger.info("替换之后的用例数据为：{}".format(case_str)) 
    # print(case_str)
    # 第四步：将完全替换后的一整个测试用例，转换回字典
    new_case_dict = eval(case_str)
    return new_case_dict
