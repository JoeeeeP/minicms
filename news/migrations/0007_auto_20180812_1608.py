# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180812_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(verbose_name='网址', max_length=256, unique=True, db_index=True),
        ),
    ]
