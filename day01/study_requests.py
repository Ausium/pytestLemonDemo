import requests

s = requests.session()

u = "url"
resq_data = {"qq":"qq"}
#登录请求
s.post(url = u ,data = resq_data)


u1 = "url01"
#因为是在上面那个会话的基础上加的一个接口，cookie已经记录在了s这个对象上，
#不用重新实例化一个对象，不然就和上一个接口的cookie没关系了，直接s.get  or  s.post等
resp = s.get(url = u1)
#获取相应状态码
print(resp.status_code)
#相应数据 -如果接口的相应数据是json格式，可以用这个方法，这个方法执行的结果是一个字典
print(resp.json())
#相应头
print(resp.headers)