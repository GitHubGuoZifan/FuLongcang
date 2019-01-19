import urllib.request
import requests
url='http://www.baidu.com/'
response=urllib.request.urlopen(url)
# content=response.read()
# print(content.decode('utf8'))
# print(response.read().decode('utf8')) #读取所有行
# print(response.readlines())  #读取所有行，返回列表
# print(response.getcode())  #获取状态码
# print(response.geturl())
# print(response.getheaders()) #获取响应头部

# with open('baidu6.html','w',encoding='utf-8') as fp :
#     fp.write(response.read().decode('utf-8'))

# with open('baidu8.html','wb') as fp :
#     fp.write(response.read())

