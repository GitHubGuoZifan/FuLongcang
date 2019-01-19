import urllib.request
import urllib.parse

#需要请求的url
post_url='https://fanyi.baidu.com/sug'
#post参数
formdata={
    'kw':'baby'
}
#构建请求对象
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

}
request=urllib.request.Request(url=post_url,headers=headers)
#发送请求，得到相应
#首先对post参数进行处理
formdata=urllib.parse.urlencode(formdata).encode('utf8')
response=urllib.request.urlopen(request,data=formdata)

print(response.read().decode('utf8'))