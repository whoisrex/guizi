# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20150929_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u6d3b\u52a8\u540d\u5b57')),
                ('type', models.PositiveIntegerField(verbose_name='\u6d3b\u52a8\u7c7b\u578b', choices=[(1, '\u4fc3\u9500'), (2, '\u4fc3\u9500'), (10, '\u5176\u4ed6')])),
                ('short_content', models.CharField(max_length=300, null=True, verbose_name='\u6d3b\u52a8\u7b80\u8981\u63cf\u8ff0')),
                ('detail_content', models.TextField(verbose_name='\u6d3b\u52a8\u8be6\u7ec6\u63cf\u8ff0')),
                ('start_at', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_at', models.DateField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('pub_to_front', models.BooleanField(verbose_name='\u662f\u5426\u53d1\u5e03\u5230\u9996\u9875')),
                ('slug', models.SlugField(max_length=100)),
                ('cover', models.ForeignKey(verbose_name='\u5c01\u9762', to='core.SimpleImage')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u6d3b\u52a8',
                'verbose_name_plural': '\u6d3b\u52a8',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
