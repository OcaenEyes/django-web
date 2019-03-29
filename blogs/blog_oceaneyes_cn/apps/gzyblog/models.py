from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.IntegerField(primary_key=id)
    tag = models.CharField(max_length=32,verbose_name="标签管理")

class Category(models.Model):
    id = models.IntegerField(primary_key=id)
    category = models.CharField(max_length=32,verbose_name="分类管理")

class Article(models.Model):
    id = models.IntegerField(primary_key=id)
    title = models.CharField(default='',max_length=20,verbose_name="文章标题")
    content = models.TextField(default='',verbose_name="文章内容")

class AdminUser(models.Model):
    id = models.IntegerField(primary_key=id)
    admin_user = models.TextField(verbose_name="文章管理")