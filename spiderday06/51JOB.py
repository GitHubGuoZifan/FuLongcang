import time
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def get_request(url,page):
    url.format(page)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    request=urllib.request.Request(url,headers=headers)
    return request

def parse_comtent(content,fp):
    soup=BeautifulSoup(content,'lxml')
    odiv=soup.find('div',id='resultList')
    div_list=odiv.find_all('div',class_='el')[1:]
    for div in div_list:
        jobname=div.select('.t1 > span >a ')[0]['title']
        company=div.select('.t2 > a')[0]['title']
        address=div.select('.t3')[0].string
        money=div.select('.t4')[0].string
        publish_time=div.select('.t5')[0].string
        item={
            '工作名称': jobname,
            '公司名称': company,
            '工作地点': address,
            '薪资': money,
            '发布时间': publish_time,
        }
        string=str(item)
        fp.write(string+'\n')

def main():
    start_page=int(input("请输入起始页："))
    end_page=int(input("请输入结束页："))
    url='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html'
    fp=open('haxi.txt','w',encoding='utf8')
    for page in range(start_page,end_page+1):
        #生成请求对象
        request=get_request(url,page)
        content=urllib.request.Request(request).read().decode('utf8')
        #解析内容
        parse_comtent(content,fp)
        time.sleep(2)
    fp.close()

if __name__ == '__main__':
    main()