import urllib.request
import json
import jsonpath

url='taobaourl'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
#创建请求对象
request=urllib.request.Request(url=url,headers=headers)
#打开请求对象，并且读取
content=urllib.request.urlopen(request).read().decode('utf8')
#去掉读取对象的内容两边多余的内容
content=content.strip('jsonp2221()\n\t\r')
#转化为json对象
obj=json.loads(content)
#找到所有的评论
comments=obj['reteDetail']['reteList']
for comment in comments:
    #评论时间
    ctime=comment['retaDate']
    #评论内容
    ccontent=comment['reteContent']
    #评论图片,这里要做判断，判断comment有没有pics这个键，用get方法，没有的话，返回none
    cimage=comment.get('pics')
    #用户（用jsonpath拿到用户名）,jsonpath取数据可以一步到位
    cname=jsonpath.jsonpath(comment,'$..displayUserNick')[0]
    print(cname)
    #保存起来