from django.contrib import admin

# Register your models here.

# -*- coding: utf-8 -*-

from django.forms import ModelForm
from suit.widgets import EnclosedInput, AutosizedTextarea, HTML5Input

from core.widget import SimditorWidget

__author__ = 'whoisrex'

from django.contrib import admin

from core.models import Article, Brand, ProductSpace, ProductType, ProductParameters, SimpleImage, Portfolio, Product, \
    Activity


class BrandForm(ModelForm):
    class Meta:
        widgets = {
            "short_intro": AutosizedTextarea(attrs={"rows": 3}),
            'quote': SimditorWidget(editor_options={'startupFocus': True})
        }


class BrandAdmin(admin.ModelAdmin):
    form = BrandForm
    search_fields = ('name', )
    list_display = ('name', 'short_content',)
    list_filter = ('name', )
    fields = ('name', 'short_content', 'story', 'cover')

    def save_model(self, request, obj, form, change):
        if request.user:
            obj.created_by = request.user
            super(BrandAdmin, self).save_model(request, obj, form, change)


class SimpleImageAdmin(admin.ModelAdmin):
    fields = ('title', 'caption', 'image', 'image_tag',)
    readonly_fields = ('image_tag',)
    list_display = ('title', 'caption', 'image_tag')

    def save_model(self, request, obj, form, change):
        if request.user:
            obj.created_by = request.user
            super(SimpleImageAdmin, self).save_model(request, obj, form, change)


class ArticleForm(ModelForm):
    class Meta:
        widgets = {
            'short_content': AutosizedTextarea(attrs={"rows": 3}),
            "detail_content": SimditorWidget(editor_options={'startupFocus': True}),
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    search_fields = ("name", 'created_by')
    list_display = ("name", 'type', 'short_content', 'created_by')
    fields = ("name", "type", "short_content", "detail_content", "cover", 'pub_to_front', 'tags', )

    def save_model(self, request, obj, form, change):
        if request.user:
            obj.created_by = request.user
            super(ArticleAdmin, self).save_model(request, obj, form, change)

class PortfolioForm(ModelForm):
    class Meta:
        widgets = {
            "detail_content": SimditorWidget(editor_options={'startupFocus': True}),
        }

class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioForm
    list_display = ("name", )
    fields = ("name", "detail_content", "gallery", "tags")

class ProductSpaceAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)

class ProductTypeAdmin(admin.ModelAdmin):
    fields = ("name", 'cover')
    list_display = ('name',)


class ProductForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={"rows": 3}),
            "prod_details": SimditorWidget(editor_options={'startupFocus': True}),
        }


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    fields = ("name", )
    search_fields = ("name", 'is_discount')
    list_display = ('name', 'type', 'brand', 'origin_price', 'is_discount')
    fields = ("name", "type", "brand", "origin_price", 'is_discount', 'new_price', 'description', 'applicable_space',
               'product_gallery', 'addition_info', 'prod_details', 'tags')

    def save_model(self, request, obj, form, change):
        if request.user:
            obj.created_by = request.user
            super(ProductAdmin, self).save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
admin.site.register(SimpleImage, SimpleImageAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductType, ProductTypeAdmin)


class ProductParametersAdmin(admin.ModelAdmin):
    fields = ("name", "value")
    list_display = ('name', 'value')


admin.site.register(ProductParameters, ProductParametersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSpace, ProductSpaceAdmin)

class ActivityForm(ModelForm):
    class Meta:
        widgets = {
            'short_content': AutosizedTextarea(attrs={"rows": 3}),
            "detail_content": SimditorWidget(editor_options={'startupFocus': True}),
        }


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityForm
    search_fields = ('name', 'type', 'created_by')
    list_display = ('name', 'type', 'short_content', 'start_at', 'end_at', 'pub_to_front', 'pub_to_banner')
    list_filter = ('name', 'type', 'pub_to_front', )
    fields = ('name', 'type', 'short_content', 'detail_content', 'start_at', 'end_at', 'cover', 'pub_to_front', 'pub_to_banner', 'promot_products', 'tags')

    def save_model(self, request, obj, form, change):
        if request.user:
            obj.created_by = request.user
            super(ActivityAdmin, self).save_model(request, obj, form, change)

admin.site.register(Activity, ActivityAdmin)
