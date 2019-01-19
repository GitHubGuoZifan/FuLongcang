import requests

url='https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6'
data={
    'ie':'utf8',
    'wd':'中国',
    'to':'en',
}
headers={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
#发送请求，params是一个原生字典
r=requests.get(url=url,params=data,headers=headers)
'''
字符串格式：r.text
字节格式：r.content
状态码：r.status_code
得到请求的url: r.url
响应头部： r.headers
设置或者获取字符集： r.encoding
'''
# r.encoding='gbk'
# print(r.headers)