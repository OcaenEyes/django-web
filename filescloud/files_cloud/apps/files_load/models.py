from django.db import models
from datetime import datetime
# Create your models here.

class Upload(models.Model):
    DownloadCount = models.IntegerField(verbose_name="访问次数",default=0)
    code = models.CharField(max_length=8,verbose_name="code")
    path = models.CharField(max_length=32,verbose_name="下载路径")
    name = models.CharField(max_length=32,verbose_name="文件名",default="")
    FileSize = models.CharField(max_length=10,verbose_name="文件大小")
    PCIP = models.CharField(max_length=32,verbose_name="IP地址",default="")

    class Meta():
        verbose_name = "download"
        db_table = "down_load"

    def __str__(self):
        return self.name
