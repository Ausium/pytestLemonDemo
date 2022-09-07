# import json

# import time

# data = [i for i in range(1,100000)]
# dJs = json.dumps(data)

# start = time.time()
# eval(dJs)
# end = time.time()
# print("eval 耗时：{}".format(end-start))
# # 输出：eval 耗时：0.18350911140441895


# start = time.time()
# json.loads(dJs)
# end = time.time()
# print("json.loads 耗时：{}".format(end-start))
# # 输出：json.loads 耗时：0.009975910186767578
import json
# d = "{'height': 1.77, 'age': 19, 'name': '张三'}"
# print(json.loads(d))
# 输出：json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

# 这个时候可以使用str的replace将单引号全部转成双引号就可以了

# 这个时候可以使用str的replace将单引号全部转成双引号就可以了
d = "{'height': 1.77, 'age': 19, 'name': '张三'}"
rep = d.replace("'",'"')
json.loads(rep)
# 输出：{'age': 19, 'height': 1.77, 'name': '张三'}

print(rep)
print(eval(rep))

# 输出：{'age': 19, 'height': 1.77, 'name': '张三'}

