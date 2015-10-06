# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u6807\u9898')),
                ('type', models.PositiveSmallIntegerField(verbose_name='\u6587\u7ae0\u680f\u76ee', choices=[(1, '\u827a\u8003\u65b0\u95fb'), (2, '\u827a\u8003\u6587\u7ae0'), (3, '\u7231\u4e50\u65f6\u5149')])),
                ('short_content', models.CharField(max_length=100, verbose_name='\u6982\u8981')),
                ('detail_content', models.TextField(verbose_name='\u6b63\u6587')),
                ('pub_to_front', models.BooleanField(verbose_name='\u662f\u5426\u53d1\u5e03\u5230\u9996\u9875')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u54c1\u724c\u540d\u79f0')),
                ('short_content', models.CharField(max_length=200, verbose_name='\u7b80\u8981\u63cf\u8ff0')),
                ('story', models.TextField(null=True, verbose_name='\u54c1\u724c\u6545\u4e8b', blank=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('like_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u6807\u9898')),
                ('short_content', models.CharField(max_length=100, verbose_name='\u6982\u8981')),
                ('detail_content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('slug', models.SlugField(max_length=100)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u9879\u76ee\u56fe\u5e93',
                'verbose_name_plural': '\u9879\u76ee\u56fe\u5e93',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5546\u54c1\u540d\u5b57')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='\u7b80\u8981\u63cf\u8ff0')),
                ('price', models.IntegerField(verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('prod_details', models.TextField(verbose_name='\u5546\u54c1\u8be6\u60c5')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ProductParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5546\u54c1\u53c2\u6570\u540d')),
                ('value', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u53c2\u6570\u503c')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u53c2\u6570',
                'verbose_name_plural': '\u5546\u54c1\u53c2\u6570',
            },
        ),
        migrations.CreateModel(
            name='ProductSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5546\u54c1\u9002\u7528\u7a7a\u95f4')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u9002\u7528\u7a7a\u95f4',
                'verbose_name_plural': '\u5546\u54c1\u9002\u7528\u7a7a\u95f4',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5546\u54c1\u79cd\u7c7b')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u79cd\u7c7b',
                'verbose_name_plural': '\u5546\u54c1\u79cd\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.PositiveIntegerField()),
                ('product', models.ForeignKey(to='core.Product')),
                ('rate_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30, blank=True)),
                ('caption', models.CharField(max_length=30, blank=True)),
                ('image', models.ImageField(upload_to=b'uploads')),
                ('thumbnail', models.ImageField(upload_to=b'uploads/thumbnails', blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
        ),
        migrations.AddField(
            model_name='producttype',
            name='cover',
            field=models.ForeignKey(to='core.SimpleImage'),
        ),
        migrations.AddField(
            model_name='product',
            name='addition_info',
            field=models.ManyToManyField(related_name='additional_info', verbose_name='\u5176\u4ed6\u53c2\u6570', to='core.ProductParameters'),
        ),
        migrations.AddField(
            model_name='product',
            name='applicable_space',
            field=models.ManyToManyField(related_name='applicable_spaces', verbose_name='\u9002\u7528\u7a7a\u95f4', to='core.ProductSpace'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(verbose_name='\u54c1\u724c', to='core.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='product_gallery',
            field=models.ManyToManyField(related_name='product_gallery', verbose_name='\u5546\u54c1\u56fe\u7247', to='core.SimpleImage'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(to='core.ProductType'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='gallery',
            field=models.ManyToManyField(related_name='gallery', verbose_name='\u56fe\u7247', to='core.SimpleImage'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='brand',
            name='cover',
            field=models.ForeignKey(verbose_name='\u54c1\u724c\u5c01\u9762', to='core.SimpleImage'),
        ),
        migrations.AddField(
            model_name='brand',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ForeignKey(verbose_name='\u5c01\u9762', to='core.SimpleImage'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
