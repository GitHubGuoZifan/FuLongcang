#测试代理能不能用

import time
import urllib.request
import random
#读取文件
fp=open('daili.txt','r')
content=fp.read()
#将内容按照换行符切割
lt=content.split('\n')
# print(lt)
while 1:
    #随机抽取一个代理，拼接为指定的格式
    daili=random.choice(lt)
    proxy={'http':daili}

    #创建handler、创建opener
    handler=urllib.request.ProxyHandler(proxies=proxy)
    opener=urllib.request.build_opener(handler)
    url='http://www.baidu.com/s?ie=UTF-8&wd=ip'
    try:
        #设置时间，请求时间超过5秒就切换到下一个
        response=opener.open(url,timeout=5)
        print('%s使用成功' % daili)
        with open('daili.html', 'wb') as fp:
            fp.write(response.read())
        break
    except Exception as e :
        print('%s使用失败' % daili)
        #将不能用的删除掉
        lt.remove(daili)
        time.sleep(2)
