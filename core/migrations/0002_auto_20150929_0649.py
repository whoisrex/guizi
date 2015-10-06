# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(verbose_name='\u5546\u54c1\u79cd\u7c7b', to='core.ProductType'),
        ),
    ]
