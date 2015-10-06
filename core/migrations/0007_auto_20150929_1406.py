# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150929_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='origin_price',
            field=models.FloatField(verbose_name='\u5546\u54c1\u4ef7\u683c'),
        ),
    ]
