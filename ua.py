import random
import urllib.request
import ssl
import random
#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url='http://www.baidu.com/'
#随机的请求对象
ua_lt=[
    'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
	'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
	'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
	'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
	'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
]
#随机选择一个UA
ua=random.choice(ua_lt)
#伪装ua，首先构建请求对象
headers={
    'User-Agent':ua,
}
#Request是一个类，它有两个参数
request=urllib.request.Request(url,headers=headers)
#headers自己定制头部，第一个参数url，第二个参数头部
#发送请求
response=urllib.request.urlopen(request)
