import requests
from lxml import etree

response = requests.get('http://www.xinpianchang.com/channel/index/id-31/sort-like')
soup = etree.HTML(response.text)
# with open('xinpian.txt','w') as f:
#     f.write(soup)
content_name_list = soup.xpath('//ul[@class="video-list"]')
content_name = ""
for i in content_name_list:
    content_name = i.xpath('.//a[@class="video-cover"]//img/@_src')
    for j in content_name:
        print(j)