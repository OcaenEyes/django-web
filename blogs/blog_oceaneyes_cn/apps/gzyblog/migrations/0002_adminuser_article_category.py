# Generated by Django 2.1.7 on 2019-03-29 12:40

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gzyblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.IntegerField(primary_key=builtins.id, serialize=False)),
                ('admin_user', models.TextField(verbose_name='文章管理')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=builtins.id, serialize=False)),
                ('article', models.TextField(verbose_name='文章管理')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=builtins.id, serialize=False)),
                ('category', models.CharField(max_length=32, verbose_name='分类管理')),
            ],
        ),
    ]
