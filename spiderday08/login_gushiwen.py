import requests
from bs4 import BeautifulSoup
import urllib.request
import time
from PIL import Image
#创建一个会话
s = requests.Session()

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
#向登陆页面发送请求，获取验证码图片链接，下载到本地
login_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r = s.get(url=login_url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
#找到图片的src
image_src = 'https://www.gushiwen.org/' + soup.find('img',id='imgCode')['src']
image_ret = s.get(image_src,headers=headers)
with open('code.png','wb') as fp:
    #content二进制网页内容
    fp.write(image_ret.content)
#将验证码图片转化为二值化图片
img = Image.open('code.png')
img = img.convert('1')
img.show()
#获取表单里面隐藏的值
viewstate = soup.find('input',id='__VIEWSTATE')['value']
viewg = soup.find('input',id='__VIEWSTATEGENERATOR')['value']

code = input('请输入验证码：')
#发送post请求
post_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
formdata = {
    '__VIEWSTATE': viewstate,
	'__VIEWSTATEGENERATOR': viewg,
	'from': 'http://so.gushiwen.org/user/collect.aspx',
	'email': '1090509990@qq.com',
	'pwd': '123456',
	'code': code,
	'denglu': '登录',
}
r = s.post(url=post_url,headers=headers,data=formdata)
print(r.text)
with open('haha.html','wb') as fp:
    fp.write(r.content)

#访问登陆成功后的页面

