from django.contrib.auth.models import AbstractUser
from django.db import models

#用户模型
class User(AbstractUser):
    qq=models.CharField(max_length=20,verbose_name="QQ号")
    tel=models.CharField(max_length=15,verbose_name="电话")
    def __str__(self):
        return self.username

    class Meta:
        verbose_name="用户"
        verbose_name_plural="用户"
        ordering=["id"]
#分类模型
class Category(models.Model):
    name=models.CharField(max_length=10,verbose_name="分类")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="分类"
        verbose_name_plural="分类"
        ordering=["id"]


#标签模型
class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name="标签名称")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name

#文章模型
class Article(models.Model):
    title=models.CharField(max_length=15,verbose_name="文章标题")
    desc=models.CharField(max_length=50,name="文章简介")
    content=models.TextField(verbose_name="文章内容")
    data_publish=models.DateField(auto_now_add=True,verbose_name="发表时间")
    click_count=models.IntegerField(verbose_name="点击量")
    user=models.ForeignKey(User,on_delete=models.CASCADE,name="所属用户")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="文章类型")
    tag=models.ManyToManyField(Tag,through="ArticleTagRelation")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="文章"
        verbose_name_plural=verbose_name
        ordering=["-data_publish","-id"]

#文章标签关系模型
class ArticleTagRelation(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)   #关联文章类型的外键类属性
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)  #关联标签类型的外键类属性

#评论模型
class Comment(models.Model):
    date_publish=models.DateField(auto_now_add=True,verbose_name="评论时间")
    content=models.TextField(verbose_name="评论内容")
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="父级评论",null=True,blank=True) #自关联
     #null是管数据库的，blank是管表单的
    def __str__(self):
        return self.content[:10]
                #最多截取10条数据
    class Meta:
        verbose_name="评论"
        verbose_name_plural=verbose_name
        ordering=["-id"]