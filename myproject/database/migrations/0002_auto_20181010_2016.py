# Generated by Django 2.0.7 on 2018-10-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': '数据', 'verbose_name_plural': '数据'},
        ),
        migrations.AlterField(
            model_name='data',
            name='update',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间'),
        ),
    ]
