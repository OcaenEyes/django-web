from django.db import models
from rest_framework.pagination import LimitOffsetPagination
# Create your models here.

class Meizitu(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    nextpage = models.CharField(db_column='nextPage', max_length=250, blank=True, null=True)  # Field name made lowercase.
    previewimg = models.CharField(db_column='previewImg', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeiZiTu'


class StandardResultPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 15