import urllib.request
# url='http://www.baidu.com/'
# response=urllib.request.urlopen(url)
# content=response.read()
# print(content.decode('utf8'))
# print(response.read().decode('utf8'))
# print(response.readlines())#读取所有行，返回列表，列表里面都是字节格式字符串
# print(response.getcode()) #获取状态码
# print(response.geturl())
# print(response.getheaders()) #获取响应头部
#写入文件第一种方式
# with open('baidu3.html','w',encoding='utf-8') as fp :
#     fp.write(response.read().decode('utf8'))
#写入文件第二种方式
# with open('baidu4.html','wb') as fp :
#     fp.write(response.read())
#图片下载第一种方式
# image_url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536587467185&di=d390a7cd933c63cd69e45feed5fcd12f&imgtype=0&src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201808%2F06%2F092308yjub8ku63b3e686j.jpg'
# response=urllib.request.urlopen(image_url)
# with open('guidao.jpg','wb') as fp :
#     fp.write(response.read())
#图片下载第二种方式
# image_url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536587467185&di=d390a7cd933c63cd69e45feed5fcd12f&imgtype=0&src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201808%2F06%2F092308yjub8ku63b3e686j.jpg'
# urllib.request.urlretrieve(image_url,'guidao2.jpg')