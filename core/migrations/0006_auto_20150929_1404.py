# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_activity_promot_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='origin_price',
        ),
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u6253\u6298'),
        ),
        migrations.AddField(
            model_name='product',
            name='new_price',
            field=models.FloatField(null=True, verbose_name='\u6253\u6298\u4ef7\u683c'),
        ),
    ]
