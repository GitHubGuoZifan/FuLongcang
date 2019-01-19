import requests

proxies={
    'http':'http://218.60.8.99:3128',
    'http':'http://118.190.217.182:80',
}
requests.get('http://www.baidu.com',proxies=proxies)