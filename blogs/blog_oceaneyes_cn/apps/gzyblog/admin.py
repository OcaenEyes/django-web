from django.contrib import admin
from .models import Tag,Category,Article,UserAccount
# Register your models here.


class TagManage(admin.ModelAdmin):
    list_display = ('id','tag')

class CategoryManage(admin.ModelAdmin):
    list_display = ('id','category')

class ArticleManage(admin.ModelAdmin):
    list_display = ('id','title','content','tag','category')
    # fields = ('id','title','content')


class UserManage(admin.ModelAdmin):
    list_display = ('id','user_name','ip')


admin.site.site_header = '乔克叔叔杂货店管理后台'
admin.site.site_title = '乔克叔叔杂货店'
admin.site.register(Tag,TagManage)
admin.site.register(Category,CategoryManage)
admin.site.register(Article,ArticleManage)
admin.site.register(UserAccount,UserManage)


