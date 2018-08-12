# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180812_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='home_display',
        ),
        migrations.RemoveField(
            model_name='column',
            name='nav_display',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(verbose_name='网址', max_length=256),
        ),
    ]
