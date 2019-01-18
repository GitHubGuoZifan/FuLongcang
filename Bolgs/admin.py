from django.contrib import admin
from Bolgs.models import *

admin.site.register([User,Category,Article,Tag,ArticleTagRelation,Comment])

