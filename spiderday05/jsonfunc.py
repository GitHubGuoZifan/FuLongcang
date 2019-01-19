import json

lt=[
    {'name':'王静','age':8,'height':130},
    {'name':'颜晓红','age':14,'height':160},
    {'name':'刘慧芬','age':18,'height':162},
]
#将对象转换为字符串，ensure_ascii，有中文的时候加
string=json.dumps(lt,ensure_ascii=False)
# 将json字符串转化为python对象
obj=json.loads(string)
print(obj)
