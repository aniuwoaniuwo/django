# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class classification(models.Model):
    name=models.CharField('分类名称',max_length=256)
    intro=models.TextField('分类简介',default='')
    slug=models.CharField('网址地址',max_length=256,db_index=True)
    administrator=models.CharField('管理员名字',max_length=256)

    def __str__(self):
        return self.name

    def getslug(self):
        return reverse('classifications',args=(self.slug,))#第一个参数是views中的name的值,意思是生成的是这个url，agrs里面的是参数

    class Meta:#这个是首页显示中文
        verbose_name = '分类'
        verbose_name_plural = '分类'


class data(models.Model):
    title = models.CharField('分类名称', max_length=256)
    type=models.ManyToManyField(classification,verbose_name='归属类型')#类型与文章是多对多关系
    content = models.TextField('内容', default='', blank=True)

    slug = models.CharField('网址地址', max_length=256, db_index=True)
    intro = models.TextField('内容简介', default='')

    author=models.CharField('作者', max_length=256)
    press=models.CharField('出版社', max_length=256)
    relevant=models.CharField('相关论文', max_length=256)

    pubdate=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update=models.DateTimeField('更新时间',auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def getdata(self):
        return reverse('data',args=(self.slug,))

    class Meta:
        verbose_name = '数据'
        verbose_name_plural = '数据'
