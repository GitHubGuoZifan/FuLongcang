import threading
from queue import Queue,Empty
import time
import requests
from bs4 import BeautifulSoup
import json

#用来标记解析线程何时退出
g_flag = True

class CrawlThread(threading.Thread):
    def __init__(self,name,page_queue,data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.url = 'http://www.fanjian.net/jianwen-{}'
        self.data_queue = data_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
    def run(self):
        print('%s线程启动'% self.name)
        '''
        1.从页码得到队列
        2.和url拼接成一个完整的url
        3.发送请求，得到响应数据
        4.将响应数据返回
        
        '''
        while 1:
            # 判断页码队列为空，线程就可以结束
            if self.page_queue.qsize() == 0:
                break
            print('开始采集数据')
            page = self.page_queue.get()
            url = self.url.format(page)
            r = requests.get(url=url,headers=self.headers)
            self.data_queue.put(r.text)
        print('{}结束线程'.format(self.name))

class ParseThread(threading.Thread):
    def __init__(self,name,data_queue,f,lock):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.f = f
        self.lock = lock

    def run(self):
        print('%s线程启动'% self.name)
        '''
        1.从数据队列中取出一页数据
        2.解析并保存数据
        '''
        while 1:
            print('进入解析内容循环')
            if g_flag == False:
                break
            try:
                print('开始解析内容')
                content = self.data_queue.get(True,3)
                self.parse_content(content)
            except Empty:
                print("--------------------")
                break
        print('%s线程结束'% self.name)

    def parse_content(self,content):
        #开始解析数据
        soup = BeautifulSoup(content,'lxml')
        #今日更新
        today_updata = soup.find('div',class_='h-updates').text
        #日期内容
        data_info = soup.find('div',class_='h-time').text
        #导航内容
        ulobj = soup.find('ul',class_='h-tablist fl clearfix')
        tablist = ulobj.find_all('a',class_='fc-gray')
        tab_list=[]
        for tab in tablist:
            tab_list.append(tab.text)

        nav_dict = {
            '今日更新': today_updata,
            '日期内容': data_info,
            '导航列表': tab_list,
        }
        #获取内容列表
        li_list = soup.select('.cont-item')
        #接收用户内容信息列表
        user_info_list = []
        for li in li_list:
            #获取头像地址
            icon = li.select('.cont-list-head > .cont-list-reward > .user-head')[0].get('href')
            #获取昵称
            username = li.select('.cont-list-head > .cont-list-reward > .user-head')[0].get('title')
            #获取标题
            title = li.select('.cont-list-title > a')[0].get('title')
            try:
                #获取内容
                content = li.select('.cont-list-main > p')[1].get_text()
            except IndexError:
                content = ''

            try:
                #获取内容图
                content_pic = li.select('.cont-list-main > p')[1].get('data-src')
            except IndexError as e :
                content_pic = ''

            content_dict = {
                '用户头像':icon,
                '用户昵称':username,
                '内容标题':title,
                '获取内容':content,
                '图片内容': content_pic,
            }
            user_info_list.append(content_dict)
        all_info_dic = {
            '导航栏':nav_dict,
            '内容': user_info_list,
        }
        #转化为json格式字符串
        string = json.dumps(all_info_dic,ensure_ascii=False)
        #上锁
        self.lock.acquire()
        #将内容写入文件
        self.f.write(string+'\n')
        self.lock.release()
        return None

def create_queue():
    page_queue = Queue()
    data_queue = Queue()

    for page in range(1,11):
        #put往队列里面添加数据
        page_queue.put(page)
    return page_queue,data_queue


def main():
    '''
    主线程的工作有：
    1.创建队列（page_queue,data_queue）
    2.创建采集线程
    3.创建解析线程
    4.启动线程
    5.主线程等待
    :return:
    '''
    # 创建队列函数
    page_queue,data_queue = create_queue()
    #打开文件
    f = open('fanjian.txt','w',encoding='utf8')
    #创建进程锁
    lock = threading.Lock()
    #创建列表用来保存所有的线程
    t_crawl_list = []
    t_parse_list = []
    # 创建所有的采集线程，并且启动
    crawl_names_list = ['采集线程1','采集线程2','采集线程3']
    for crawl_name in crawl_names_list:
        t_crawl = CrawlThread(crawl_name,page_queue,data_queue)
        t_parse_list.append(t_crawl)
        t_crawl.start()
    #创建所有的解析线程，并且启动
    parse_names_list = ['解析线程1','解析线程2','解析线程3']
    for parse_name in parse_names_list:
        t_parse = ParseThread(parse_name,data_queue,f,lock)
        t_parse_list.append(t_parse)
        t_parse.start()

    #一直判断页码队列是否为空
    while 1:
        if page_queue.empty():
            break
    time.sleep(3)
    while 1:
        if data_queue.empty():
            global g_flag
            g_flag = False
            break
    #主线程等待子线程
    for t_crawl in t_crawl_list:
        t_crawl.join()

    for t_parse in t_parse_list:
        t_parse.join()
    f.close()
    print('主线程-子线程结束')

if __name__ == '__main__':
    main()