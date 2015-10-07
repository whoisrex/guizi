# -*- coding: utf-8 -*-
from datetime import date

import os
import random
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, connection

# Create your models here.
from django.db.models import QuerySet, Count, Q
from django.db.models.fields.files import ImageFieldFile
from taggit.managers import TaggableManager
import time
from uuslug import uuslug
from guizi import settings


def group_by(query_set, group_by):
    '''util:django 获取分类列表'''
    assert isinstance(query_set, QuerySet)
    django_groups = query_set.values(group_by).annotate(Count(group_by))
    groups = []
    for dict_ in django_groups:
        groups.append(dict_.get(group_by))
    return groups


def get_tagclouds():
    cursor = connection.cursor()
    cursor.execute(
        "select count(A1.tag_id) as count, A2.name as tag_name, A2.slug as tag_slug, A1.tag_id  from taggit_taggeditem A1, taggit_tag A2 where A1.tag_id = A2.id group by A1.tag_id order by count DESC limit 6")
    data = cursor.fetchall()
    return data


class TracableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    class Meta:
        abstract = True

class Like(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    like_by = models.ForeignKey(User)


class LikeModel(models.Model):
    likes = generic.GenericRelation(Like)

    def get_like_count(self):
        a_type = ContentType.objects.get_for_model(self)
        count = Like.objects.filter(content_type__pk=a_type.id, object_id=self.id).count()
        return count

    def is_liked_by_user(self, user):
        a_type = ContentType.objects.get_for_model(self)
        likes = Like.objects.filter(content_type__pk=a_type.id, object_id=self.id, like_by=user)
        return len(likes) != 0

    def be_liked(self, liked_by):
        a_type = ContentType.objects.get_for_model(self)
        flag = "D"
        try:
            like = Like.objects.get(content_type__pk=a_type.id,  object_id=self.id, like_by=liked_by)
            like.delete()
        except ObjectDoesNotExist:
            like = Like(content_object=self)
            like.like_by = liked_by
            like.save()
            flag = "A"

        count = self.get_like_count()
        return {"count": count, "flag": flag}

    @classmethod
    def get_hot(cls, max_size=6):
        a_type = ContentType.objects.get_for_model(cls)
        like_query = Like.objects.filter(content_type__pk=a_type.id)
        hots = group_by(like_query, 'object_id')
        size = len(hots)
        if size < max_size:
            hots = hots[0:size]
        else:
            hots = hots[0:max_size]
        hotest = cls.objects.filter(id__in=hots)
        return hotest

    class Meta:
        abstract = True


class SimpleImage(TracableMixin):
    title = models.CharField(max_length=30, blank=True)
    caption = models.CharField(max_length=30, blank=True)

    image = models.ImageField(upload_to=settings.UPLOAD_TO)
    thumbnail = models.ImageField(upload_to=settings.THUMBNAIL_ROOT, blank=True)

    def __unicode__(self):
        return self.image.url

    def image_tag(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe('<img src="%s" sizes="%s"/>') % (self.thumbnail.url, '20%')
        else:
            return u'请上传图片'

    image_tag.allow_tags = True
    image_tag.short_description = u'图片'

    def save(self):
        base, ext = os.path.splitext(os.path.basename(self.image.path))

        fn = time.strftime("%Y%m%d%H%M%S")
        fn = fn + "%d" % random.randint(0,100)

        self.image.name = fn + ext

        pixbuf = Image.open(self.image)
        width, height = pixbuf.size
        if width > settings.THUMBNAIL_SIZE:
            delta = width / settings.THUMBNAIL_SIZE
            height = int(height / delta)
            pixbuf.thumbnail((settings.THUMBNAIL_SIZE, height), Image.ANTIALIAS)

        relate_thumb_path = os.path.join(settings.THUMBNAIL_ROOT, fn + '.thumb' + ext)
        thumb_path = os.path.join(settings.MEDIA_ROOT, relate_thumb_path)
        pixbuf.save(thumb_path)

        self.thumbnail = ImageFieldFile(self, self.thumbnail, relate_thumb_path)
        super(SimpleImage, self).save()

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'

ARTICLE_TYPE = (
    (1, u'艺考新闻'),
    (2, u'艺考文章'),
    (3, u'爱乐时光'),
)


class Article(LikeModel, TracableMixin):
    name = models.CharField(max_length=20, verbose_name=u"标题")
    type = models.PositiveSmallIntegerField(u'文章栏目', choices=ARTICLE_TYPE)
    short_content = models.CharField(max_length=100, verbose_name=u"概要")
    detail_content = models.TextField(verbose_name=u"正文")
    cover = models.ForeignKey(SimpleImage, verbose_name=u"封面")

    pub_to_front = models.BooleanField(u"是否发布到首页")
    slug = models.SlugField(max_length=100, db_index=True)
    tags = TaggableManager()

    @classmethod
    def get_recommended(cls):
        recommended = Article.objects.filter(pub_to_front=True).order_by("-created_at")
        return recommended

    def get_related_articles(self):
        names = self.tags.names
        related_articles = Article.objects.filter(tags__name__in=names).exclude(id=self.id).distinct()
        if related_articles and len(related_articles) > 3:
            return related_articles[0:3]
        else:
            return related_articles

    def get_next_article(self):
        try:
            q = Article.objects.filter(Q(id__lt=self.id), Q(type=self.type)).order_by("-id")[0]
            return q
        except IndexError:
            return None

    def get_previous_article(self):
        try:
            q = Article.objects.filter(Q(id__gt=self.id), Q(type=self.type)).order_by("id")[0]
            return q
        except IndexError:
            return None

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Article, self).save(*args, **kwargs)


class Portfolio(LikeModel, TracableMixin):
    name = models.CharField(max_length=20, verbose_name=u"标题")
    short_content = models.CharField(max_length=100, verbose_name=u"概要")
    detail_content = models.TextField(verbose_name=u"内容")
    gallery = models.ManyToManyField(SimpleImage, related_name="gallery", verbose_name=u'图片')

    slug = models.SlugField(max_length=100, db_index=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = u'项目图库'
        verbose_name_plural = u'项目图库'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Portfolio, self).save(*args, **kwargs)

    @classmethod
    def get_latest(cls, max_size=6):
        queryset = Portfolio.objects.all()
        size = len(queryset)
        if size < max_size:
            hots = queryset[0:size]
        else:
            hots = queryset[0:max_size]
        return hots



class Brand(LikeModel, TracableMixin):
    name = models.CharField(u'品牌名称', max_length=30)
    short_content = models.CharField(u'简要描述', max_length=200)
    story = models.TextField(u'品牌故事', null=True, blank=True)
    cover = models.ForeignKey(SimpleImage, verbose_name=u'品牌封面')
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'品牌'
        verbose_name_plural = u'品牌'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Brand, self).save(*args, **kwargs)


class ProductType(models.Model):
    name = models.CharField(u'商品种类', max_length=30)
    cover = models.ForeignKey(SimpleImage)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'商品种类'
        verbose_name_plural = u'商品种类'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(ProductType, self).save(*args, **kwargs)


class ProductSpace(models.Model):
    name = models.CharField(u'商品适用空间', max_length=30)
    cover = models.ForeignKey(SimpleImage)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'商品适用空间'
        verbose_name_plural = u'商品适用空间'

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(ProductSpace, self).save(*args, **kwargs)

class ProductParameters(models.Model):
    name = models.CharField(u'商品参数名', max_length=30)
    value = models.CharField(u'商品参数值', max_length=50)

    def __unicode__(self):
        return self.name + ":" + self.value

    class Meta:
        verbose_name = u'商品参数'
        verbose_name_plural = u'商品参数'

class Product(LikeModel, TracableMixin):
    name = models.CharField(u'商品名字', max_length=30)
    type = models.ForeignKey(ProductType, verbose_name=u"商品种类")
    brand = models.ForeignKey(Brand, verbose_name=u'品牌')
    description = models.CharField(u'简要描述', max_length=300, null=True)
    product_gallery = models.ManyToManyField(SimpleImage, related_name="product_gallery", verbose_name=u'商品图片')
    origin_price = models.FloatField(u'商品价格')
    is_discount = models.BooleanField(u"是否打折", default=False, db_index=True)
    new_price = models.FloatField(u"打折价格", blank=True, null=True)
    prod_details = models.TextField(u'商品详情')
    applicable_space = models.ManyToManyField(ProductSpace, related_name="applicable_spaces", verbose_name=u"适用空间")
    addition_info = models.ManyToManyField(ProductParameters, related_name="additional_info", verbose_name=u"其他参数")

    tags = TaggableManager()

    def get_cover_url(self):
        return self.product_gallery.first().image.url

    def get_avg_rate(self):
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(rate) as avg_rate FROM core_rate WHERE product_id = %s", [self.id])
        row = cursor.fetchone()
        return row[0]

    @classmethod
    def sort_by_price(cls):
        products = Product.objects.all().order_by("price")
        return products

    @classmethod
    def sort_by_popularity(cls):
        pass

    @classmethod
    def get_recent_products(cls, max_size=6):
        recent_products = Product.objects.all()
        if recent_products and len(recent_products) > max_size:
            return recent_products[0:max_size]
        else:
            return recent_products

    def get_related_products(self, max_size=6):
        names = self.tags.names
        related_products = Product.objects.filter(tags__name__in=names).exclude(id=self.id).distinct()
        if related_products and len(related_products) > max_size:
            return related_products[0:max_size]
        else:
            return related_products

    def __unicode__(self):
        return self.type.name +" : " + self.name

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品'

class Rate(models.Model):
    product = models.ForeignKey(Product)
    rate = models.PositiveIntegerField()
    rate_by = models.ForeignKey(User)

    @classmethod
    def get_most_rated_products(cls, max_size=6):
        queryset = Rate.objects.all()
        hots = group_by(queryset, 'product')
        size = len(hots)
        if size < max_size:
            hots = hots[0:size]
        else:
            hots = hots[0:max_size]

        return hots


THE_ACTIVITY_TYPE = (
    (1, u'促销'),
    (2, u'促销'),
    (10, u'其他'),
)


class Activity(TracableMixin):
    name = models.CharField(u'活动名字', max_length=30)
    type = models.PositiveIntegerField(u"活动类型", choices=THE_ACTIVITY_TYPE)
    short_content = models.CharField(u'活动简要描述', max_length=300, null=True)
    detail_content = models.TextField(verbose_name=u"活动详细描述")
    cover = models.ForeignKey(SimpleImage, verbose_name=u"封面")

    start_at = models.DateField(verbose_name=u"开始时间")
    end_at = models.DateField(verbose_name=u"结束时间")
    promot_products = models.ManyToManyField(Product, related_name="promot_products", verbose_name=u"参加活动商品")

    pub_to_front = models.BooleanField(u"是否发布到首页广告")
    pub_to_banner = models.BooleanField(u"是否发布到横幅广告")

    slug = models.SlugField(max_length=100, db_index=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'活动'
        verbose_name_plural = u'活动'
        ordering = ['-created_at']

    @classmethod
    def get_banner_activity(cls):
        banner_activity = Activity.objects.filter(Q(pub_to_banner=True))
        return banner_activity

    @classmethod
    def get_shop_promot_acitivity(cls):
        front_activity = Activity.objects.filter(Q(pub_to_front=True))
        return front_activity

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Activity, self).save(*args, **kwargs)