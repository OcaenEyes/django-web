from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=32,verbose_name="标签管理")

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=32,verbose_name="分类管理")

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(default='',max_length=20,verbose_name="文章标题")
    tag = models.CharField(max_length=32, verbose_name="标签管理", default='')
    category = models.CharField(default='', max_length=32, verbose_name="分类管理")
    author = models.CharField(default='', verbose_name="作者", max_length=10)
    image = models.ImageField(upload_to='images',verbose_name="封面图片",null=True)
    abstract = models.TextField(default='',verbose_name="摘要",max_length=100)
    content = models.TextField(default='',verbose_name="文章内容")
    create_time =models.DateTimeField(verbose_name="创建时间",default=timezone.now())
    update_time = models.DateTimeField(verbose_name="最近编辑时间",auto_now=True)


class UserAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name= models.CharField(max_length=20,verbose_name="用户名")
    ip = models.GenericIPAddressField(protocol='ipv4',default='')

class Reward(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(default='',max_length=20,verbose_name="求赞语言")
    qrcode = models.ImageField(upload_to='qrcode',verbose_name="二维码",null=True)

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(default='',max_length=10,verbose_name="图片描述")
    image = models.ImageField(upload_to='images',verbose_name="素材图片")


