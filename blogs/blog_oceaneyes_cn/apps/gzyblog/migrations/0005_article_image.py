# Generated by Django 2.1.3 on 2019-03-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gzyblog', '0004_auto_20190329_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='封面图片'),
        ),
    ]