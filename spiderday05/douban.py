import urllib.request
import json
from lxml import etree
#因为豆瓣电影使用ajax方法进行的局部加载，所以进入网页之后，要点击检查，然后在XHR里面找你想要的内容
url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=100&page_start=0'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

request=urllib.request.Request(url=url,headers=headers)
content=urllib.request.urlopen(request).read().decode('utf8')
#content就是json格式的字符串
lt=[]
#将其转化为python对象
obj=json.loads(content)
#遍历这个列表,,,通过字典的键，去查找它的值
for movie in obj["subjects"]:
    #要海报
    image_src=movie['cover']
    #要电影名字
    title=movie['title']
    #要评分
    score=movie['rate']
    #评价人数
    count=movie['cover_x']
    item={
        '电影海报':image_src,
        '电影名字':title,
        '电影评分':score,
        '评价人数':count
    }
    lt.append(item)
#将lt保存到文件中
string=json.dumps(lt,ensure_ascii=False)
with open('movie.txt','w',encoding='utf8') as fp:
    fp.write(string)
