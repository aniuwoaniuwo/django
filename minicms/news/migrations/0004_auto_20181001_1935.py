# Generated by Django 2.0.7 on 2018-10-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180929_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
        migrations.AddField(
            model_name='column',
            name='nva_display',
            field=models.BooleanField(default=False, verbose_name='导航显示'),
        ),
    ]
