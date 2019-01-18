
#这个文件夹主要是为了存储文章的评论信息，用到了递归函数，因为在一篇文章下面写的评论，还有人会对评论进行评论
#把这个函数封装起来，那么下次在页面上用的时候就不会那么乱，则直接调这个函数就可以了

def find_parent_comment(comment_tree,comment): #这个函数传两个参数，第一个是评论树，第二个是子评论
    for p,v in comment_tree.items(): # iteams是一个元组，第一个个是它的键，第二个是它的值
        if p==comment.parent_comment:  #如果p等于评论的父评论
            comment_tree[p][comment]={}  #p是父评论，comment是传个来的形参，把评论树的父评论和子评论放到一个字典里面
            break
        else:
            find_parent_comment(comment_tree[p],comment)
            #如果被遍历的不在评论树，那么把它设置成父评论，
def create_comment(comments):
    comment_tree={}  #将要填充的评论树
    for comment in comments:  #遍历该文章下的所有评论
        if comment.parent_comment is None:   #如果父评论为None，说明是一级评论
            comment_tree[comment]={}   #将一级评论作为评论树的键
        else:
            find_parent_comment(comment_tree,comment)

    return comment_tree

# def fact(5):
#     return fact_iter(5,1)
#
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
#                     5,1
#                     4,5
#                     3,20
#                     2,60
#                     1,120
#                     120