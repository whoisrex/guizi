# -*- coding: utf-8 -*-
import json

from django import http
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from core.models import SimpleImage, Article, Product, Brand, ProductType, Rate, Portfolio
from guizi import settings
# Create your views here.


class FrontBadRequest(http.HttpResponseBadRequest):
    def __init__(self, why):
        super(FrontBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("500.html", {"why": why})

# @cache_page(60 * 15)
def home(request):
    if request.user:
        most_rated_products = Rate.get_most_rated_products(max_size=4)
        most_hot_products = Product.get_hot(max_size=4)
        return render(request, "welcome.html", {"most_rated_products": most_rated_products, "most_hot_products": most_hot_products})
    else:
        return render(request, "home.html")

def uploads(request):
    file = request.FILES.get("Filedata")
    if file:
        upload = SimpleImage(title="", caption="", image=file)
        upload.save()

        response_data ={}
        response_data["file_path"] = upload.image.url
        response_data["success"] = True
        response_data["result"] = 1
        response_data['pic_id'] = upload.id
        return HttpResponse(json.dumps(response_data), content_type="application/json")

ARTICLE_PAGE_SIZE = 10


def blog(request):
    type = request.GET.get('t')
    page = request.GET.get('p')
    paginator = Paginator(Article.objects.filter(type=2), ARTICLE_PAGE_SIZE)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(paginator.num_pages)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, "core/article.html", {"page": blog_list,  "type": "blog"})

def article_info(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, "core/article_info.html", {"article": article, 'next': True, 'url': request.get_full_path()})


def shop(request):
    list = []
    brands = Brand.objects.all()
    product_types = ProductType.objects.all()
    products = Product.get_hot(max_size=12)
    return render(request, "core/shop.html", {"products":products, "brands": brands, "product_types":product_types,  "count": len(list)})


def brand(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    return render(request, "core/shop_products_base.html", {"item": brand, 'title': brand.name, 'next': True, 'url': request.get_full_path()})

def type(request, type_slug):
    type = get_object_or_404(ProductType, slug=type_slug)
    return render(request, "core/shop_products_base.html", {"item": type, 'title': type.name, 'next': True, 'url': request.get_full_path()})

def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    is_like = product.is_liked_by_user(request.user)
    return render(request, "core/shop_single.html", {"product": product, 'is_like': is_like, 'next': True, 'url': request.get_full_path()})

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, "core/portfolio.html", {"portfolios": portfolios})

@login_required
def like(request):
    if request.user.is_authenticated():
        type = request.POST.get("type")
        id = request.POST.get("id")
        if type == "product":
            response_data = get_object_or_404(Product, id=id).be_liked(request.user)
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        redirect("/user/signin/")

def aboutus(request):
    return render(request, "core/about-us.html")

def contact(request):
    return render(request, "core/contact-us.html")