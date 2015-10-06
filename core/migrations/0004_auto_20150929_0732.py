# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150929_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='pub_to_banner',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u53d1\u5e03\u5230\u6a2a\u5e45\u5e7f\u544a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='pub_to_front',
            field=models.BooleanField(verbose_name='\u662f\u5426\u53d1\u5e03\u5230\u9996\u9875\u5e7f\u544a'),
        ),
    ]
