import requests
from requests.exceptions import Timeout

url='http://www.baidu.com/'
headers={

}
try:
    r=requests.get(url=url,headers=headers,timeout=0.01)

except Timeout as e:
    print(e)