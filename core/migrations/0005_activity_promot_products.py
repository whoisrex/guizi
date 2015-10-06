# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150929_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='promot_products',
            field=models.ManyToManyField(related_name='promot_products', verbose_name='\u53c2\u52a0\u6d3b\u52a8\u5546\u54c1', to='core.Product'),
        ),
    ]
