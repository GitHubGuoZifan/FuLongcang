import urllib.request
# 设置代理
#创建handler
handler=urllib.request.ProxyHandler(proxies={'http':'218.60.8.99：3129'})
opener=urllib.request.build_opener(handler)
url='http://www.baidu.com/s?ie=UTF-8&wd=ip'
response=opener.open(url)
with open('daili.html','wb') as fp:
    fp.write(response.read())