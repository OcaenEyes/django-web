# Generated by Django 2.1.3 on 2019-03-30 11:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gzyblog', '0010_auto_20190330_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 11, 2, 14, 32763, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]