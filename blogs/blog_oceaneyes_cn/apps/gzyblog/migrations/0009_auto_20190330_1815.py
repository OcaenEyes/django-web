# Generated by Django 2.1.7 on 2019-03-30 10:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gzyblog', '0008_auto_20190330_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(default='', max_length=10, verbose_name='图片描述')),
                ('image', models.ImageField(upload_to='images', verbose_name='素材图片')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 10, 15, 47, 165015, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
