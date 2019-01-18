from django.urls import path
from Bolgs.views import *
app_name="Bolgs"
urlpatterns =[
    path('',index,name="index"),
    path('category_articles/<cid>/',category_article,name="category_articles"),
    path('page_articles/',article_page,name="page_article"),
    path('article/<aid>/',getarticle_byid,name="article"),
    path('login/',login,name="login"),
    path('reg/',reg,name="reg"),
    
]