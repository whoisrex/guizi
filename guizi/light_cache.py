from core.models import Article, get_tagclouds, Activity, ProductType, ProductSpace, Brand, Portfolio
from django.core.cache import cache

__author__ = 'functionality@sina.com'

def get_pop_articles():
    articles = cache.get("pop_articles_news")
    if not articles:
        articles = Article.get_recommended(type=1)
        # cache.set("pop_articles", articles)
    return articles

def get_pop_tips():
    articles = cache.get("pop_articles_tips")
    if not articles:
        articles = Article.get_recommended(type=2)
        # cache.set("pop_articles", articles)
    return articles

def get_banner_activities():
    banner_activities = cache.get("banner_activities")
    if not banner_activities:
        banner_activities = Activity.get_banner_activity()
        # cache.set("pop_articles", articles)
    return banner_activities

def get_shop_promotion_activities():
    shop_promot_activities = cache.get("banner_activities")
    if not shop_promot_activities:
        shop_promot_activities = Activity.get_shop_promot_acitivity()
        # cache.set("pop_articles", articles)

    return shop_promot_activities

def get_recent_articles():
    articles = cache.get("recent_articles")
    if not articles:
        articles = Article.objects.all()
        # cache.set("recent_articles", articles)
    return articles

def get_tag_cloud():
    tags = cache.get("tag_cloud")
    if not tags:
        tags = get_tagclouds()
        # cache.set("tag_cloud", tags)
    return tags


def get_product_types():
    product_types = cache.get("product_types")
    if not product_types:
        product_types = ProductType.objects.all()
        # cache.set("product_types", product_types)
    return product_types

def get_brands():
    brands = cache.get("brands")
    if not brands:
        brands = Brand.objects.all()
        # cache.set("brands", brands)
    return brands

def get_spaces():
    spaces = cache.get("spaces")
    if not spaces:
        spaces = ProductSpace.objects.all()
        # cache.set("spaces", spaces)
    return spaces

def get_portfolio_carousels():
    portfolios = cache.get("portfolio_carousels")
    if not portfolios:
        portfolios = Portfolio.get_latest(max_size=3)
        # if len(testimonials) > 3:
        #     testimonials = testimonials[0:3]
        # cache.set("portfolio_carousels", testimonials)

    return portfolios
