from django.contrib import admin
from .models import Youone

# Register your models here.


class YouoneManage(admin.ModelAdmin):
    list_display = ('imgurl','textnum','imgauther','mon','day')

admin.site.register(Youone,YouoneManage)