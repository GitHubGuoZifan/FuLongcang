from queue import Queue
from queue import Empty
import threading
from threading import Condition
import time
import requests
from bs4 import BeautifulSoup

condition = Condition()


class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jianwen-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

    def run(self):
        print('%s线程启动------' % self.name)
        '''
        1、从页码队列中取一个页码
        2、和url拼接成一个完整的url
        3、发送请求，得到响应数据
        4、将响应数据存放到数据队列中
        '''
        while True:
            try:
                page = self.page_queue.get(True, 10)
                url = self.url.format(page)
                r = requests.get(url=url, headers=self.headers)
                self.data_queue.put(r.text)
            except Empty as e:
                print(e)
                break
        print('%s线程结束--' % self.name)


class ParseThread(threading.Thread):
    def __init__(self, name, data_queue, fp, lock, page_queue):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.page_queue = page_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('%s线程启动------' % self.name)
        '''
        1、从数据队列取出一页数据
        2、解析并保存数据
        '''

        # while not self.data_queue.empty():
        while True:
            try:
                content = self.data_queue.get(True, 10)
                self.parse_content(content)
            except Empty as e:
                print(e)
                break
        print('%s线程结束--' % self.name)

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # 解析即可
        soups = soup.select("body > div.page > div.page-body.clearfix > div.main > div > div.b > ul > li > h2 > a")

        for x in soups:
            href = x['href']
            title = x["title"]
            text = x.string
            resurlt = str({"href": href, "title": title, "text": text}) + "\n"
            print(title)
            self.lock.acquire()
            # 写入文件
            print(resurlt)
            self.fp.write(resurlt)

            self.lock.release()


# 创建队列函数
def create_queue():
    page_queue = Queue()
    for page in range(1, 50):
        page_queue.put(page)
    data_queue = Queue()
    return page_queue, data_queue


def main():
    # 主线程。主线程的工作都有哪些？
    # 创建队列，页码队列、数据队列
    page_queue, data_queue = create_queue()
    # 打开文件
    fp = open('jian.txt', 'w', encoding='utf8')
    lock = threading.RLock()
    '''
    1、创建采集线程
    2、创建解析线程
    3、启动线程
    4、主线程等待
    '''
    # 创建列表，用来保存所有的线程
    t_crawl_list = []
    t_parse_list = []
    # 创建所有的采集线程，并且启动之
    crawl_names_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_names_list:
        t_crawl = CrawlThread(crawl_name, page_queue, data_queue)
        t_crawl_list.append(t_crawl)
        t_crawl.start()

    # 创建所有的解析线程，并且启动之
    parse_names_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_names_list:
        t_parse = ParseThread(parse_name, data_queue, fp, lock, page_queue)
        t_parse_list.append(t_parse)
        t_parse.start()

    # 主线程等待子线程
    for t_crwl in t_crawl_list:
        t_crwl.join()
    for t_parse in t_parse_list:
        t_parse.join()
    fp.close()

    print('主线程-子线程全部结束')


if __name__ == '__main__':
    # condition = Condition()
    # singal = threading.Event()
    main()
