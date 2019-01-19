from selenium import webdriver

sel =webdriver.Chrome()
sel.get('https://www.dianping.com/')
sel.find_element_by_xpath('//*[@id="top-nav"]/div/div[2]/span[2]/a[1]').click()
# 切入嵌套frame
sel=switch_to.frame('//*[@id="J_login_container"]/div/iframe')