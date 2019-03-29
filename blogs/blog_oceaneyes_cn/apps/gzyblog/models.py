from django.db import models

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
    content = models.TextField(default='',verbose_name="文章内容")
    tag = models.CharField(max_length=32, verbose_name="标签管理",default='')
    category = models.CharField(default='',max_length=32, verbose_name="分类管理")


class UserAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name= models.CharField(max_length=20,verbose_name="用户名")
    ip = models.GenericIPAddressField(protocol='ipv4',default='')
