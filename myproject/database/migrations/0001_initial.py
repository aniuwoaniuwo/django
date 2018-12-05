# Generated by Django 2.0.7 on 2018-10-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='分类名称')),
                ('intro', models.TextField(default='', verbose_name='分类简介')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='网址地址')),
                ('administrator', models.CharField(max_length=256, verbose_name='管理员名字')),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='分类名称')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='网址地址')),
                ('intro', models.TextField(default='', verbose_name='内容简介')),
                ('author', models.CharField(max_length=256, verbose_name='作者')),
                ('press', models.CharField(max_length=256, verbose_name='出版社')),
                ('relevant', models.CharField(max_length=256, verbose_name='相关论文')),
                ('pubdate', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update', models.DateTimeField(auto_now_add=True, null=True, verbose_name='跟新时间')),
                ('type', models.ManyToManyField(to='database.classification', verbose_name='归属类型')),
            ],
        ),
    ]