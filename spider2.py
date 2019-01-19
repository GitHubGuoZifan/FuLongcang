import urllib.parse

# string='username=周杰伦&password=12345'
# url='http://www.baidu.com/index.html?'
# ret=string=urllib.parse.quote(string)
# 编码函数
# ret=urllib.parse.quote('http://www.baidu.com/index.html?username=狗蛋&pwd=123')
#解码函数
# ret=urllib.parse.unquote('http://www.baidu.com/index.html?username=狗蛋&pwd=123')
# print(ret)
url='http://www.baidu.com/index.html?'
dudu='王力宏'
lala='18'
weight='170'
# #get参数写法
data={
    'name':dudu,
    'age':lala,
    'weight':weight,
}#先将参数写成一个字典
# ret=urllib.parse.urlencode(data)
# url+=ret
# print(url)

#拼接路径
# lt=[]
# for k,v in data.items():
#     lt.append(k+'='+v)
# url+='&'.join(lt)
# print(url)
#编码函数(对URl中的中文进行编码)
# ret = urllib.parse.quote('http://www.baidu.com/index.html?username=狗蛋&pwd=123')
# print(ret)
#解码函数
# ret=urllib.parse.unquote('http://www.baidu.com/index.html?username=狗蛋&pwd=123')
# print(ret)
#get参数写法
url='http://www.baidu.com/index.html?'
dudu='王力宏'
lala='18'
weight='170'
data={
    'name':dudu,
    'age':lala,
    'weight':weight,
}
ret=urllib.parse.urlencode(data)
url+=ret
print(url)