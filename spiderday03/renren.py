#通过代码访问个人资料页
import urllib.request

url='http://www.renren.com/960481378/profile'
headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'Connection': 'keep-alive',
	'Cookie': 'anonymid=jlyk7a6d-xf0g2p; depovince=GW; jebecookies=880cec8e-b699-42e3-897a-ab29f0790af3|||||; _r01_=1; JSESSIONID=abc3rsWw_PDTRbJSPUlxw; ick_login=4d7fac5d-c2c0-44fb-bd2d-15367f4088f0; _de=F872F5698F7602B30ADE65415FC01940; p=76f69863171d82d497ff3cd38c3301978; first_login_flag=1; ln_uact=17701256561; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=9292d7e743133988ada1f34c35acaba98; societyguester=9292d7e743133988ada1f34c35acaba98; id=960481378; xnsid=344518e8; ver=7.0; loginfrom=null; jebe_key=8a462ca1-5793-4e6e-a08a-ad63b85b9b23%7C86ba94a3b75a9848502e25ac92562959%7C1536721351507%7C1%7C1536721352729; wp_fold=0',
	'Host': 'www.renren.com',
	'Referer': 'http://www.renren.com/960481378',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)

with open('renren.html','wb') as fp :
    fp.write(response.read())