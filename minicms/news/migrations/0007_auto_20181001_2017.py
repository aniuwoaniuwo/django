# Generated by Django 2.0.7 on 2018-10-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20181001_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='nva_display',
            new_name='nav_display',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=200, unique=True, verbose_name='网址'),
        ),
    ]
