from django.db import models
from rest_framework.pagination import LimitOffsetPagination

# Create your models here.
class Youone(models.Model):
    imgurl = models.CharField(db_column='imgUrl', max_length=250, blank=True, null=True)  # Field name made lowercase.
    textnum = models.CharField(db_column='textNum', max_length=250, blank=True, null=True)  # Field name made lowercase.
    imgauther = models.CharField(db_column='imgAuther', max_length=250, blank=True, null=True)  # Field name made lowercase.
    textcontent = models.CharField(db_column='textContent', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mon = models.CharField(max_length=250, blank=True, null=True)
    day = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YOUONE'


class StandardResultSetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 15