
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼到配置文件路径
conf_dir = os.path.join(basedir, "Conf")

# 拼接  测试数据路径
def testdata_dir():
    testdata_dir = os.path.join(basedir, "Excle_test")
    return os.path.join(testdata_dir,"test.xlsx")


# 日志路径
log_dir = os.path.join(basedir, "outputs", "logs")

# 报告路径
def report_dir():
    report_dir = os.path.join(basedir, "outputs", "reports")


# # 1、basedir
# basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# def get_confPath():
#     # 拼到配置文件路径
#     conf_dir = os.path.join(basedir, "Conf")
#     return conf_dir

# # 拼接  测试数据路径
# def get_testDataPath():
#     testdata_dir = os.path.join(basedir, "Excle_test")
#     return testdata_dir

# # 日志路径
# def get_logPath():
#     log_dir = os.path.join(basedir, "outputs", "logs")
#     return log_dir

# # 报告路径
# def get_logPath():
#     report_dir = os.path.join(basedir, "outputs", "reports")
#     return report_dir