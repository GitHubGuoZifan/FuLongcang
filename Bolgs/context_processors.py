from DjangoBlogs import settings
from Bolgs.models import Category

def global_settings(request):
    BLOG_NAME=settings.BLOG_NAME
    BLOG_DESC=settings.BLOG_DESC
    category_list=Category.objects.all()
    return locals()



@login_required(login_url='/login/')  # 该装饰器会影响重定向位置，调试时注释掉它
def child_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            try:
                cd = comment_form.cleaned_data
                user = request.POST['author']
                mesg = cd['comment']
                art = int(request.POST.get('artid'))
                parent = int(request.POST.get('commentid'))
                childid = int(request.POST.get('childid'))
                parent_comt = Comment.objects.get(id=parent)
                child_comt = ChildrenComment.objects.get(id=childid)
                ChildrenComment.objects.create(username=user, child_mesg=mesg,
                child_comt=child_comt,parent_comt=parent_comt)
                return HttpResponseRedirect('/article/%d/'%art)
            except TypeError:
                return HttpResponse('cunchu失败')
        else:
            return HttpResponse('评论失败')
    else:
        comment_form = CommentForm()
        art = int(request.GET.get('artid'))
        parent = int(request.GET.get('commentid'))
        childid = int(request.GET.get('childid'))
        return render(request, 'childcomment.html', locals())