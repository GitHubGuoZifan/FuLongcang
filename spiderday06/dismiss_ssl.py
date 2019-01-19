import requests
requests.packages.urllib3
url='http://www.12306.cn/'
#verify=False,忽略证书
r=requests.get(url,verify=False)