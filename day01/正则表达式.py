import re
s = "qqq4#sa#fasd#fsd#fsdf#s#d#1#q#q#"
# if re.match("q",s):
#     print("true")
# else:
#     print("false")
res = re.findall("#\w*#",s)
print(res)