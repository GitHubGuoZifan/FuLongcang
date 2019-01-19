from selenium import webdriver #通过浏览器的对象实现你的一些上网的操作
import time
path=r'D:\feiq\Recv Files'
#创建谷歌浏览器对象
browser=webdriver.Chrome(executable_path=path)

#通过浏览器对象上网
url='http://www.baidu.com/'
#打开这个地址
browser.get(url)
time.sleep(3)

#找到输入框，往里面写东西
my_input=browser.find_element_by_id('kw')
#往里面些内容
my_input.send_keys('美女')
time.sleep(2)

#点击百度一下按钮
my_button=browser.find_element_by_id('su')
my_button.click()
time.sleep(3)

a_href=browser.find_elements_by_xpath()[0]
#有s的时候要加0，没有s就不用加了
a_href.click()
time.sleep(2)
# browser.find_elements_by_xpath   根据xpath路径查找指定节点
# browser.find_elements_by_id    根据id查找指定节点
# browser.find_elements_by_css_selector
# browser.find_elements_by_link_text()
# 推出浏览器
# browser.quit()