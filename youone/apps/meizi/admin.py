from django.contrib import admin
from .models import Meizitu

# Register your models here.

class MztuManage(admin.ModelAdmin):
    list_display = ('date','title','nextpage','previewimg')

admin.site.register(Meizitu,MztuManage)