import urllib.request
import re
import os
import time
#根据指定的url生成请求对象并且返回
def generate_request(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

#得到响应内容
def get_response(request):
    response=urllib.request.urlopen(request)
    return response.read().decode('utf8')

def parse_content(content):
    '''
    <div class="thumb">

<a href="/article/120983427" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12098/120983427/medium/2BTDL0YEQXN7P7X9.jpg" alt="真是笑死了">
</a>

</div>
    '''
    pattern=re.compile(r'<div class="thumb">.*?<img src=(.*?) alt=(.*?)>.*?</div>',re.S)
    ret=pattern.findall(content)
    #根据列表，下载所有的图片
    down_load(ret)

def down_load(ret):
    dirname='qiutu'
    for tp in ret:
        #取出图片地址
        image_src='http:'+tp[0].strip("\"")
        print(image_src)
        #取出图片名字
        title=tp[1]
        print(title)
        #strip里面的双引号是转义的意思，意思是把你的URL内容转化为字符串
        filename=title.strip("\"\" /")+'.' + image_src.split('.')[-1]
        print(filename)
        filepath=os.path.join(dirname,filename)
        print('正在下载图片：%s...' % filename)
        urllib.request.urlretrieve(image_src,filepath)
        print('结束下载图片%s'% filename)
        time.sleep(2)

def main():
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))
    # start_page = 1
    # end_page=1
    url='https://www.qiushibaike.com/pic/page/'
    for page in range(start_page,end_page+1):
        print('正在下载第%s页...' % page)
        new_url=url+str(page)+'/'
        request=generate_request(new_url)
        #发送请求，得到响应内容，字符串
        content=get_response(request)
        #写正则表达式，解析网页内容
        parse_content(content)
        print('结束下载第%s页....'% page)
        time.sleep(2)


if __name__ == '__main__':
    main()
