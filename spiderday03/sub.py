import re

string='男人都喜欢20岁的女孩'
pattern=re.compile(r'\d+')
# ret=pattern.sub('50',string)
# print(ret)
#在原来的基础上加1
#该函数必须有一个参数，是一个对象
#该函数必须有一个返回值，是字符串，用返回值替换匹配的内容
#obj是
def fn(obj):
    num=int(obj.group())+1
    return str(num)

ret=pattern.sub(fn,string)