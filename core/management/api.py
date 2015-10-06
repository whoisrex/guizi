# -*- coding: utf-8 -*-
from tastypie.authorization import Authorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL

__author__ = 'whoisrex'

from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from core.models import Product, Brand, SimpleImage, Portfolio, ProductType, ProductSpace, Article

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'email', 'date_joined', 'last_login']

class ProductTypeResource(ModelResource):
    class Meta:
        queryset = ProductType.objects.all()
        # list_allowed_methods = ['get', 'post']
        resource_name = 'type'



class ProductSpaceResource(ModelResource):
    class Meta:
        queryset = ProductSpace.objects.all()
        # list_allowed_methods = ['get', 'post']
        resource_name = 'productspace'
        authorization = Authorization()
        filtering = {'productspace': ALL}


class ImageResource(ModelResource):
    class Meta:
        queryset = SimpleImage.objects.all()
        resource_name = 'image'
        filtering = {'image': ALL}


class BrandResource(ModelResource):
    cover = fields.ForeignKey(ImageResource, 'cover', null=True)

    class Meta:
        queryset = Brand.objects.all()
        resource_name = 'brand'
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        return super(BrandResource, self).obj_create(bundle, created_by=bundle.request.user)


class ProductResource(ModelResource):
    type = fields.ForeignKey(ProductTypeResource, 'type', null=True)
    brand = fields.ForeignKey(BrandResource, 'brand', null=True)
    product_gallery = fields.ManyToManyField(ImageResource, 'image', null=True)
    applicable_space = fields.ManyToManyField(ProductSpaceResource, 'productspace', null=True)

    class Meta:
        queryset = Product.objects.all()
        list_allowed_methods = ['post', 'get', 'patch', 'put']
        resource_name = 'product'
        filtering = {
                'product_gallery': ALL_WITH_RELATIONS,
                'applicable_space': ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, **kwargs):
        return super(ProductResource, self).obj_create(bundle, created_by=bundle.request.user)


class ArticleResource(ModelResource):
    cover = fields.ForeignKey(ImageResource, 'cover', null=True)

    class Meta:
        queryset = Article.objects.all()
        list_allowed_methods = ['post', 'get', 'patch', 'put']
        resource_name = 'article'
        authorization = Authorization()

    def obj_create(self, bundle, **kwargs):
        return super(ArticleResource, self).obj_create(bundle, created_by=bundle.request.user)


class PortfolioResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'project'
        authorization = Authorization()
    def obj_create(self, bundle, **kwargs):
        return super(BrandResource, self).obj_create(bundle, created_by=bundle.request.user)

