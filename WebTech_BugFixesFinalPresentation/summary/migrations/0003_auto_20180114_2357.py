# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookId',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subjectId',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='summaryId',
        ),
        migrations.RemoveField(
            model_name='university',
            name='universityId',
        ),
    ]
