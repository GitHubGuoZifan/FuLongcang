#复杂的get
import urllib.request
import urllib.parse
import os
import time

baname=input('请输入贴吧的名字')
start_page=int(input('请输入起始页码'))
end_page=int(input('请输入结束页码'))

url='http://baidu.tieba.com/f?'

for page in range(start_page,end_page+1):
    print('开始下载第%s页。。。'%page)
    pn=(page-1)*50

    data={
        'kw':baname,
        'ie':'utf8',
        'pn':pn,
    }
    query_string = urllib.parse.urlencode(data)
    url_tmp = url + query_string
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    request=urllib.request.Request(url=url_tmp,headers=headers)
    response=urllib.request.urlopen(request)
    if not os.path.exists(baname):
        os.mkdir(baname)

    #生成文件名
    filename='%s-第%s页.html'%(baname,page)
    filepath=os.path.join(baname,filename)
    with open(filepath,'wb') as fp:
        fp.write(response.read())
    print('结束下载第%s页'% page)
    time.sleep()