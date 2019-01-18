from django.core.paginator import Paginator,PageNotAnInteger

#这个函数封装了上下页的功能
def getblog_bypage(article_list,page_number):
    try:
        paginator=Paginator(article_list,2)  #实例化分页器对象
        page=paginator.page(page_number)   #获取某一页的数据
    except PageNotAnInteger:       #传过来的参数不是一个整型的话
        page=paginator.page(1)     #那么给它默认是第一页的数据
    return page        #返回到页面被遍历的page