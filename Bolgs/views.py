from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from Bolgs.blog_page import getblog_bypage
#导入这个文件的这个类，因为要调用这个文件里面的函数
from Bolgs.models import *

#显示文章的标题
def index(request):
    article_list=Article.objects.all()  #获取文章表的全部内容
    page=getblog_bypage(article_list,1)   #调用这个函数对文章表的内容进行分页管理
    return render(request,'index.html',locals())
# #点击文章标题显示它所对应的文章
# def category_article(request,cid):
#     article_list=Article.objects.get(category_id=cid)
#     # page=getblog_bypage(article_list,1)
#     return render(request,'index.html',locals())
# #点击“上一页”，“下一页”获取对应的文章
# def article_page(request):
#     page_number=int(request.GET.get("page",1))
#     cid=request.GET['cid']
#     if cid:
#         article_list=Article.objects.filter(category_id=cid)
#     else:
#         article_list=Article.objects.all()
#     page=getblog_bypage(article_list,page_number)
#     return render(request,'index.html',locals())
#
# #显示标签名
# def getarticle_byid(request,aid):
#     article=Article.objects.get(id=aid)
#     return render(request,'article.html',locals() )
# #登陆
# def login(request):
#     login_name=request.POST["Username"]
#     login_pwd=request.POST["Password"]
#     user_queryset=User.objects.filter(username=login_name,password=login_pwd)
#     if user_queryset:
#         request.session["loginname"]=login_name
#         return HttpResponseRedirect("/Bolgs/")
#     else:
#         return render(request,"login.html",{"msg":"用户名或密码错误，请重新登陆！  "})
#
# #注册
# def reg(request):
#     regName=request.POST.get("regname")
#     regpwd=request.POST.get("regpwd")
#     regemail=request.POST.get("regemail")
#     regqq=request.POST.get("regqq")
#     user=User.objects.create(username=regName,password=regpwd,email=regemail,qq=regqq)
#     return render(request,"Bolgs/login.html",locals())
#
# def getarticle_byid(request,aid):
#     article =Article.objects.get(id=aid)
#     comments=article.comment_set.all() #获取该文章对应的所有评论
#     # print("该文章对应的所有评论是：",comments)
#     # comment_tree=create_comment_tree(comments)  #创建评论树
#     # print("最终的评论树是：",comment_tree)
#     return render(request,'article.html',locals())


def article(request,cid):
    if request.method=='GET':
        article=Article.objects.get(article_id=cid)
        article.click_count+=1    #点击量自加一
        article.save()
        comment_list=article.arttable.all()  #???
        comment_form=Comment()   #???
        return render(request,'article.html',locals())
    else:
        return HttpResponseRedirect('/')

def register(request):
    if request.method=='POST':
        tel=request.POST.get('tel')
        qq=request.POST.get('qq')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.create_user(username=username,password=password,
                                          tel=tel,qq=qq,email=email)
            login(request,user)  #???
            return HttpResponseRedirect('/')
        except:
            return HttpResponse("注册失败")
    else:
        return render(request,'reg.html')

def logoutview(request):  #???
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def comment(request):
    if request.method=='POST':
        comment_form=Comment(request.POST)
        if comment_form.is_valid():
            try:
                cd=comment_form.cleaned_data
                user=request.POST['author']
                mesg=cd['comment']
                art=int(request.POST['art'])
                article=Article.objects.get(id=art)
                Comment.objects.create(user=user,mesg=mesg,comt=article)
                return HttpResponseRedirect('/article/%d/'&art)  #???
            except TypeError:
                return HttpResponse('存储失败')
        else:
            return HttpResponse('评论失败')
    else:
        comment_form=Comment()
        return render(request,'article.html',locals())

@login_required(login_url='/login/')
def child_comment(request):
    if request.method=='POST':
        comment_form=Comment(request.POST)
        if comment_form.is_valid()
            try:
                cd=comment_form.cleaned_data
                user=request.POST['author']
                mesg=cd['comment']
                art=int(request.POST.get('commentid'))
                parent_comt=Comment.objects.get(id=parent)
                child_comt=Comment.objects.get(id=childid)
                Comment.objects.create(username=user,child_comment=mesg,
                child_comt=child_comt,parent_comt=parent_comt)
                return HttpResponseRedirect('/article/%d/'%art)
            except TypeError:
                return HttpResponse('存储失败')
        else:
            return HttpResponse('评论失败')
    else:
        comment_form=Comment()
        art=int(request.GET.get('cid'))
        parent=int(request.GET.get('commentid'))
        childid=int(request.GET.get('childid'))
        return render(request,'childcomment.html',locals())