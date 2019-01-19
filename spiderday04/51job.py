import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
'''
https://mkt.51job.com/tg/sem/pz_2018.html?from=baidupz
'''

def get_request(url,page):
    #拼接url .format替换掉
    url=url.format(page)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def parse_content(content,fp):
    #生成soup对象
    soup=BeautifulSoup(content,'lxml')
    odiv=soup.find('div',id='resultList')
    #找到所有的div
    div_list=odiv.find_all('div',class_='el')[1:]
    #遍历每一个div，获取每一份工作的信息
    print(div_list[0])
    for div in div_list:
        jobname=div.select('.t1 > span > a')[0]['title']
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
        fp.write(string + '\n')


def main():
    # start_page=int(input('请输入起始页码：'))
    # end_page=int(input('请输入结束页码:'))
    start_page = 1
    end_page = 2
    url='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html'
    #打开文件
    fp=open('haha.txt','w',encoding='utf8')
    for page in range(start_page,end_page+1):
        #生成请求对象
        request=get_request(url,page)
        #发送请求，得到响应内容
        content=urllib.request.urlopen(request).read().decode('gbk')
        #解析内容(就是把爬取的内容写到文件里面)
        parse_content(content,fp)
        print('结束爬取第%s页...'% page)
        time.sleep(2)
    fp.close()

if __name__ == '__main__':
    main()