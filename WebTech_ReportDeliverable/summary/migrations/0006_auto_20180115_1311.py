# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-15 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
