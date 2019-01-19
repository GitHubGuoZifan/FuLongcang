from selenium import webdriver
import time
url='http://www.baidu.com/'
path=r'D:\feiq\Recv Files\phantomjs-2.1.1-windows\bin\phantomjs.exe'

#创建浏览器对象
browser=webdriver.PhantomJS(executable_path=path)
browser.get(url)

time.sleep(3)
browser.save_screenshot('pic')
#模拟滚动条到底部（在js里面就是一段代码）
# 网页卷起的高度 scrollTop,网页的高度
#第二个可以写body,也可以写documentElement
js='document.body.scrollTop=10000'
#让phantomjs执行这个代码
browser.execute_script(js)
time.sleep(4)
browser.save_screenshot('./pic/douban2.png/')
#得到执行完js之后的代码  ,browser.page_source
with open('douban.html','w',encoding='utf8') as fp:
    fp.write(browser.page_source)
#第二种方式
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(browser.page_source,'lxml')
    browser.quit()