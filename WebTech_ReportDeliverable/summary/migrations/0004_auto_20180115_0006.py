# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0003_auto_20180114_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='university',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='book',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='university',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
