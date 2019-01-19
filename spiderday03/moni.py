import http.cookiejar
import urllib.request
import urllib.parse
#在代码中如何保存cookie,携带cookie
#创建一个cookiejar对象
#cj是用来保存cookie的
cj=http.cookiejar.CookieJar()
#通过cj创建一个handler
handler=urllib.request.HTTPCookieProcessor(cj)
opener=urllib.request.build_opener(handler)

# 在往下所有的请求都使用opener.open()方法发送，那么就会自动保存cookie和携带cookie

post_url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201883115448'
formdata={
'email': '17701256561',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'password': '416f0c7ccd370d88b6c15b1bbff0f328583a8bce638bada6b5b3b345696c4c35',
	'rkey': 'cac8af90965f6d9819e7956057ea478d',
	'f': 'http%3A%2F%2Fwww.renren.com%2F960481378%2Fprofile',
}
formdata=urllib.parse.urlencode(formdata).decode('utf8')
headers={
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
request=urllib.request.Request(url=post_url,headers=headers)
response=opener.open(request,data=formdata)
print(response.read().decode('utf8'))

#访问登陆后的页面
pro_url=''
request=urllib.request.Request(url=pro_url,headers=headers)
response=opener.open(request)

with open('renren2.html','wb') as fp:
    fp.write(response.read())