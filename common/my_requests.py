import os
import sys
sys.path.append(os.getcwd())

from ssl import ALERT_DESCRIPTION_USER_CANCELLED
import requests
import pytest
import os
from common.myConf import MyConf
from common.my_path import conf_dir


class MyRequests:

    #初始化方法
    def __init__(self):

        #请求头
        self.headers = {"Content-type": "application/json"} 
        #属性
        #方法 post/get/put... json=xxx,params=xxx

        # def send_requests(self,url,method,json=None,params=None):
        #     #调用requests的方法发起一个请求，并得到响应结果
        #     resp = requests.request(method,url,json=json,params=params,headers=self.headers)

        #读取配置文件中的server
        self.base_url = MyConf(os.path.join(conf_dir,"conf.ini")).get("server","host")

    def send_requests(self,api_url,method,data,token=None):
        #处理请求头
        self.__deal_header(token)

        #处理请求url
        self.__deal_url(api_url)

        if method.upper() == "GET":
            resp = requests.request(method,self.url,params=data,headers=self.headers)
        else: 
            resp = requests.request(method,self.url,json=data,headers=self.headers)
        return resp

    def __deal_header(self,token=None):
        if token:
            self.headers["Authorization"] = "Bearer {}".format(token)

    def __deal_url(self,api_url):
        url = self.base_url + api_url
        self.url = url


if __name__ == '__main__':
    mr = MyRequests()
    url = "api/v1/pub/login/3rd"
    req_data = {"ID": "chenzanxu","secret": "25d55ad283aa400af464c76d713c07ad", "type": "default"}
    method = "post"
    reps = mr.send_requests(url,method,req_data)
    print(reps.json())