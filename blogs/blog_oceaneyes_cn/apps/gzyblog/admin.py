from django.contrib import admin
from .models import Tag,Category,Article,AdminUser
# Register your models here.

class TagManage(admin.ModelAdmin):
    list_display = ('id','tag')

class CategoryManage(admin.ModelAdmin):
    list_display = ('id','category')

class ArticleManage(admin.ModelAdmin):
    list_display = ('id','title','content')

class AdminUserManage(admin.ModelAdmin):
    list_display = ('id','admin_user')

admin.site.register(Tag,TagManage)
admin.site.register(Category,CategoryManage)
admin.site.register(Article,ArticleManage)
admin.site.register(AdminUser,AdminUserManage)