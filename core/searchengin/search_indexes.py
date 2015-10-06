# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from models import Article, Activity, Portfolio, Client
from haystack import indexes


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='created_by')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录


class ActivityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='created_by')

    def get_model(self):
        return Activity

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录


class PortfolioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Portfolio

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录


class ClientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="name")
    intro = indexes.CharField(model_attr="short_intro")

    def get_model(self):
        return Client

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
