import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class ZhiLianSpider():
    #构造方法，将传递过来的参数一一的保存到成员属性中
    def __init__(self,jl,kw,start_page,end_page):
        self.jl=jl
        self.kw=kw
        self.start_page=start_page
        self.end_page=end_page
        #起始url
        self.url='https://sou.zhaopin.com/?'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

    def get_request(self,page):
        #拼接url
        #get的参数字典为
        data={
            'jl':self.jl,
            'kw':self.kw,
            'p':page,
        }
        query_string=urllib.parse.urlencode(data)
        url=self.url+query_string
        request=urllib.request.Request(url=url,headers=self.headers)
        return request

    def parse_content(self,content):
        with open('lala.txt','w',encoding='utf8') as fp:
            fp.write(content)
            #生成soup对象
            soup=BeautifulSoup(content,'lxml')
            #提取数据
            #首先提取到所有的table
            odiv=soup.find('div',class_='newlist_list')

    def run(self):
        #将代码跑起来
        for page in range(self.start_page,self.end_page+1):
            #拼接url,生成请求对象并且返回
            request=self.get_request(page)
            #得到网页内容字符串
            content=urllib.request.urlopen(request).read().decode('utf8')
            #解析网页内容
            self.parse_content(content)

def main():
    #工作地点
    jl=input('请输入工作地点：')
    kw=input('请输入搜索关键字：')
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))
    obj=ZhiLianSpider(jl,kw,start_page,end_page)
    obj.run()

if __name__ == '__main__':
    main()