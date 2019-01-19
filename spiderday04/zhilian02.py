import urllib.request
from bs4 import BeautifulSoup

url=''
headers={

}
request=urllib.request.Request(url=url,headers=headers)
content=urllib.request.urlopen(request).read().decode('utf8')
with open('lala.html','w',encoding='utf8') as fp:
    fp.write(content)