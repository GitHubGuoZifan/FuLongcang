import urllib.request

url='http://www.baidu.com/'

#创建handler
handler=urllib.request.HTTPHandler()
#通过handler创建一个opener
opener=urllib.request.build_opener(handler)
#这个opener有一个叫做open的方法，就是以前你用的urlopen()
response=opener.open(url)
print(response.read().decode('utf8'))