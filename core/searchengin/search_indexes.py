# -*- coding: utf-8 -*-
from core.models import Article, Portfolio, Product

__author__ = 'Administrator'


from haystack import indexes


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    author = indexes.CharField(model_attr='created_by')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    type = indexes.CharField(model_attr='type')
    author = indexes.CharField(model_attr='created_by')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录


class PortfolioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='title')

    def get_model(self):
        return Portfolio

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录

