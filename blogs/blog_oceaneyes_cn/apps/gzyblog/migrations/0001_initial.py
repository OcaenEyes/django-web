# Generated by Django 2.1.3 on 2019-03-31 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='文章标题')),
                ('tag', models.CharField(default='', max_length=32, verbose_name='标签管理')),
                ('category', models.CharField(default='', max_length=32, verbose_name='分类管理')),
                ('author', models.CharField(default='', max_length=10, verbose_name='作者')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='封面图片')),
                ('abstract', models.TextField(default='', max_length=100, verbose_name='摘要')),
                ('content', models.TextField(default='', verbose_name='文章内容')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2019, 3, 31, 10, 11, 38, 26330, tzinfo=utc), verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最近编辑时间')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=32, verbose_name='分类管理')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(default='', max_length=10, verbose_name='图片描述')),
                ('image', models.ImageField(upload_to='images', verbose_name='素材图片')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='求赞语言')),
                ('qrcode', models.ImageField(null=True, upload_to='qrcode', verbose_name='二维码')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=32, verbose_name='标签管理')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('ip', models.GenericIPAddressField(default='', protocol='ipv4')),
            ],
        ),
    ]
