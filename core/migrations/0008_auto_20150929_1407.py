# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150929_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.FloatField(null=True, verbose_name='\u6253\u6298\u4ef7\u683c', blank=True),
        ),
    ]
