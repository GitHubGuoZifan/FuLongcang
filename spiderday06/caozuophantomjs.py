import time
from selenium import webdriver

path=r'D:\feiq\Recv Files\phantomjs-2.1.1-windows\bin\phantomjs.exe'

#创建浏览器对象
browser=webdriver.PhantomJS(executable_path=path)
url='http://www.baidu.com/'
browser.get(url)

time.sleep(3)
#拍个照片，留个纪念
browser.save_screenshot('pic')
#打开输入框，输入美女           #输入的内容
browser.find_element_by_id('kw').send_keys('男子汉')
time.sleep(3)
browser.find_element_by_id('su').click()
time.sleep(3)
browser.save_screenshot('pic')
browser.quit()