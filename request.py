import urllib.request
url='http://www.baidu.com/'
response=urllib.request.urlopen(url)
# print(response)
# 获取得到相应的内容,得到的是二进制格式的字符串
# content=response.read()


'''
（二进制格式）---》字符串格式
.decode('utf8')
（字符串格式）---》二进制格式
'''
# print(content.decode('utf8'))
# print(response.read().decode('utf8'))
# print(response.readlines())
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())
#写入文件第一种方式
# with open('baidu1.html','w',decoding='utf-8') as fp:
#     fp.write(response.read().decode('utf8'))

#写入文件第二种方式
# with open('baudu2.html','wb') as fp:
    # fp.write(response.read())

#图片下载
# image_url='http://i1.umei.cc/uploads/tu/201608/12/u2cj1dv00oa.jpg'
# response=urllib.request.urlopen(image_url)
#将响应内容写到文件中
# with open('meinv.jpg','wb') as fp:
#     fp.write(response.read())

#图片下载第二种方式
image_url='http://i1.umei.cc/uploads/tu/201702/473/slt16.png'
urllib.request.urlretrieve(image_url,'meinv2.jpg')

