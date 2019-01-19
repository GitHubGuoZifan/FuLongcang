import urllib.request
import urllib.parse

print('每页显示十条')
page=int(input('请输入要显示的页数：'))
#根据页树计算start和limit
'''
page=1  0,10
page=2= 10,20
page=3  20,10
page=n  (n-1)*10,10


'''
start=(page-1)*10
limit=10
#get参数
data={
    'start':start,
    'limit':limit,
}
url='https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=160&limit=20'
#拼接url
url+=urllib.parse.urlencode(data)
print(url)
headers={
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

}
#构建请求对象
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
print(response.read().decode('utf8'))

#没出来