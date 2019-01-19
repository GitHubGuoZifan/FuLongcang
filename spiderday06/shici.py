import pymongo
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#创建mongodb的连接对象


client=pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db = client.test
#指定集合,这样声明了一个Collection对象
collection = db.students

#insert插入数据
# result=collection.insert(student)

class ZhiLianSpider(object):
    def __init__(self,jl,kw,start_page,end_page):
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.url = 'https://sou.zhaopin.com/?pageSize=60&jl=530&kw=Python&kt=3'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }

    def get_request(self,page):
        data = {
            'jl':self.jl,
            'kw':self.kw,
            'p':page,
        }
        query_string = urllib.parse.urlencode(data)
        url = self.url + query_string
        request = urllib.request.Request(url=url,headers=self.headers)
        jobs = {
            'url':url,

        }
        collection.insert(jobs)
        return request
    def parse_content(self,content):
        with open('lala.txt','w',encoding='utf8') as fp:
            fp.write(content)
        soup = BeautifulSoup(content,'lxml')
        odiv = soup.find('div',class_='newlist_list')

    def run(self):
        for page in range(self.start_page,self.end_page):
            request = self.get_request(page)
            content = urllib.request.urlopen(request).read().decode('utf8')
            self.parse_content(content)

def main():
    jl = input('请输入工作地点：')
    kw = input('请输入搜索关键字：')
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    obj = ZhiLianSpider(jl,kw,start_page,end_page)
    obj.run()
    client.close()

if __name__ == '__main__':
    main()
