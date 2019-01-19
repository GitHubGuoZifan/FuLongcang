import urllib.request
import urllib.parse

post_url=''

cname=input('请输入要查询的城市')
pageIndex=input('请输入页码')
pageSize=input('请输入个数')
formdata={

}
#处理表单数据

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}