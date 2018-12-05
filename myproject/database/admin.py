from django.contrib import admin
from .models import data,classification

class classificationshow(admin.ModelAdmin):
    list_display=('name','administrator','intro')

class datashow(admin.ModelAdmin):
    list_display = ('title','slug','author','intro','press','pubdate','update')#type不能显示，因为是多对多的关系

admin.site.register(data,datashow)
admin.site.register(classification,classificationshow)