import urllib.request
import urllib.parse

#输入您要查询的关键字
kw= input('请输入要搜索的内容')
#get参数
data={
    'ie':'utf8',
    'wd':kw,
} #kw指的是文件名
url='https://www.baidu.com/s?'
#首先将data转化为query_string格式
query_string=urllib.parse.urlencode(data)
#拼接url
url+=query_string
#构建请求对象
headers={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)

#发送请求对象，得到相应对象
response=urllib.request.urlopen(request)

#将内容写到文件中
filename=kw+'.html'
with open(filename,'wb') as fp:
    fp.write(response.read())