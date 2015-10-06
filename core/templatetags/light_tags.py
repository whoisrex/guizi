from django.template.loader import render_to_string
from guizi import light_cache as cache
from core.models import Article

__author__ = 'Administrator'

from django import template

register = template.Library()


@register.tag
def render_article_sidebar(parser, token):
    return ArticleSideBar()


class ArticleSideBar(template.Node):
    def render(self, context):
        pop_articles = cache.get_pop_articles()
        recent_articles = cache.get_recent_articles()
        template_search_list = [
            "core/article_sidebar.html",
        ]
        liststr = render_to_string(template_search_list, {
            "pop_articles": pop_articles, 'recent_articles': recent_articles,
        }, context)
        return liststr

@register.tag
def render_tagcloud_widget(parser, token):
    return TagCloudWidget()


class TagCloudWidget(template.Node):
    def render(self, context):
        tag_cloud = cache.get_tag_cloud()
        template_search_list = [
            "core/tagcloud_widget.html",
        ]
        liststr = render_to_string(template_search_list, {
            "tag_cloud": tag_cloud,
        }, context)
        return liststr


@register.tag
def render_related_article(parser, token):
    # {% render_related_article for obj %}
    tokens = token.split_contents()
    if tokens[1] != 'for':
        raise template.TemplateSyntaxError("Second argument in %r tag must be 'for'" % tokens[0])

    if len(tokens) == 3:
        article = tokens[2]
        return RelatedArticleTag(article)
    else:
        raise template.TemplateSyntaxError("Third argument in %r tag must be 'for'" % tokens[2])


class RelatedArticleTag(template.Node):

    def __init__(self, article):
        self.article = article

    def render(self, context):
        article = context[self.article]
        related_articles = article.get_related_articles()
        template_search_list = [
            "core/related_articles.html",
        ]
        liststr = render_to_string(template_search_list, {
            "related_articles": related_articles
        }, context)
        return liststr


# @register.tag
# def render_testimonials_widget(parser, token):
#     return TestimonialsWidget()
#
#
# class TestimonialsWidget(template.Node):
#     def render(self, context):
#         testimonials = cache.get_testimonials()
#         template_search_list = [
#             "core/testimonials_widget.html",
#         ]
#         liststr = render_to_string(template_search_list, {
#             "testimonials": testimonials
#         }, context)
#         return liststr


@register.tag
def render_article_slider(parser, token):
    return ArticleSlider()

class ArticleSlider(template.Node):
    def render(self, context):
        pop_articles = cache.get_pop_articles()
        template_search_list = [
            "core/article_slider.html",
        ]
        liststr = render_to_string(template_search_list, {
            "pop_articles": pop_articles
        }, context)
        return liststr


@register.tag
def render_shop_slider(parser, token):
    return ShopSlider()

class ShopSlider(template.Node):
    def render(self, context):
        promotions = cache.get_banner_activities()
        template_search_list = [
            "core/shop_slider.html",
        ]
        liststr = render_to_string(template_search_list, {
            "promotions": promotions
        }, context)
        return liststr


@register.tag
def render_shop_promo(parser, toekn):
    return ShopPromotSection()

class ShopPromotSection(template.Node):
    def render(self, context):
        promotions = cache.get_shop_promotion_activities()
        template_search_list = [
            "core/shop_promot_section.html",
        ]
        liststr = render_to_string(template_search_list, {
            "promotions": promotions
        }, context)
        return liststr


@register.tag
def render_portfolio_carousel_widget(parser, token):
    return PortfolioCarouselWidget()

class PortfolioCarouselWidget(template.Node):
    def render(self, context):
        portfolios = cache.get_portfolios()
        template_search_list = [
            "core/portfolio_carousel.html",
        ]
        liststr = render_to_string(template_search_list, {
            "portfolios": portfolios
        }, context)
        return liststr

@register.tag
def render_shop_sidebar(parser, token):
    return ShopSideBar()

class ShopSideBar(template.Node):
    def render(self, context):
        product_types = cache.get_product_types()
        brands = cache.get_brands()
        spaces = cache.get_spaces()
        template_search_list = [
            "core/shop_sidebar.html",
        ]
        liststr = render_to_string(template_search_list, {
            "product_types": product_types, "brands": brands, "spaces":spaces
        }, context)
        return liststr

@register.tag
def render_related_products(parser, token):
    # {% render_related_article for obj %}
    tokens = token.split_contents()
    if tokens[1] != 'for':
        raise template.TemplateSyntaxError("Second argument in %r tag must be 'for'" % tokens[0])
    if len(tokens) == 3:
        product = tokens[2]
        return RelatedProductsTag(product)
    else:
        raise template.TemplateSyntaxError("Third argument in %r tag must be 'for'" % tokens[2])


class RelatedProductsTag(template.Node):
    def __init__(self, product):
        self.product = product

    def render(self, context):
        product = context[self.product]
        related_products = product.get_related_products()
        template_search_list = [
            "core/related_products.html",
        ]
        liststr = render_to_string(template_search_list, {
            "related_products": related_products
        }, context)
        return liststr



