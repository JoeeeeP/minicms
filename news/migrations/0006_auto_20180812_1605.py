# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180812_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(verbose_name='首页显示', default=False),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(verbose_name='导航显示', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(verbose_name='网址', max_length=256, db_index=True),
        ),
    ]
