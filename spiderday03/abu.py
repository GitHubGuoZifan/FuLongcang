import base64
import urllib.request

url='https://www.baidu.com/?tn=80035161_1_dg'
user='H29P184OL9R0755D'
pwd='9642800C88B2EED9'
string='user'+':'+'pwd'
#Base64编码是一种防君子不防小人的编码方式
#优点：速度快,ascii字符，肉眼不可理解
#缺点：编码比较长，比较容易被破解，仅适用于加密非关键信息的场合
#b64encode函数的参数为byte类型，所以必须先转码
#将指定的字符串进行base64编码
encodestr='Basic'+ base64.b64decode(string.encode('utf8')).decode('utf8')

headers={
    'Proxy-Authorization': encodestr,
}
#构建请求对象
request=urllib.request.Request(url=url,headers=headers)

#构建handler,构建opener
proxy={'http':'http-dyn.abuyun.com:9020'}
handler=urllib.request.ProxyHandler(proxies=proxy)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
with open('daili.html','wb') as fp:
    fp.write((response.read()))