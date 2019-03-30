# Generated by Django 2.1.3 on 2019-03-30 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gzyblog', '0005_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='求赞语言')),
                ('qrcode', models.ImageField(null=True, upload_to='qrcode', verbose_name='二维码')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=10, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 6, 32, 11, 465424, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最近编辑时间'),
        ),
    ]
