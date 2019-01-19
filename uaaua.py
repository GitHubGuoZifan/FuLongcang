import urllib.request
import urllib.parse

kw=input('请输入要搜索的内容：')
#字典里面写的是路径后面的参数
data={
	'ie':'utf8',
	'wd':kw,
}
url='http://www.baidu.com/s?'
query_string=urllib.parse.urlencode(data)
url+=query_string
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)
filename=kw+'.txt'
with open(filename,'wb') as fp:
	fp.write(response.read())