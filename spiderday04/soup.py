from bs4 import BeautifulSoup

#生成对象
soup=BeautifulSoup(open('haha.html',encoding='utf8'),'lxml')
#soup是一个官方对象，不是字符串，但是打印的是字符串
# ret=soup.a
# print(ret.attrs['href'])
# ret=soup.div
# print(ret.string)
# print(ret.text)
# print(ret.get_text())
# ret=soup.find('a',id='mu')
# ret=soup.find('li',title='bai')
# print(ret)
# odiv=soup.find('div',id='song')
# ret=soup.find('li',id='qing')
# print(ret)
# ret=soup.find_all('a')
# print(ret[-3]['href'])
# ret=soup.find_all(['a','li'])
# print(ret)
# ret=soup.find_all('a',class_='bai',limit=1)
# print(ret)
# import re
# odiv=soup.find('div',class_='tang')
# ret=odiv.find_all('li',class_=re.compile('^dudu'))
# print(ret)
# ret=soup.select('#qing')
# print(ret[0].string)
# ret=soup.select('.bai')
# print(ret)

ret=soup.select('li')
print(ret)