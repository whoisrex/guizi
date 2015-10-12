# -*- coding: utf-8 -*-
import json

from django import http
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from core.models import SimpleImage, Article, Product, Brand, ProductType, Rate, Portfolio, ProductSpace, Activity
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
        recent_portfolios = Portfolio.get_latest(max_size=4)
        recent_articles = Article.get_recommended()
        activities = Activity.get_banner_activity()
        types = ProductType.objects.all()

        return render(request, "welcome.html", {"most_rated_products": most_rated_products,
                        "recent_articles": recent_articles, "types": types, 'activities': activities,  "recent_portfolios": recent_portfolios, "most_hot_products": most_hot_products})
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
    paginator = Paginator(Article.objects.filter(type=type), ARTICLE_PAGE_SIZE)
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(paginator.num_pages)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, "core/article.html", {"page": blog_list,  "type": type})

def article_info(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, "core/article_info.html", {"article": article, 'next': True, 'url': request.get_full_path()})


def activity_infor(request, activity_slug):
    item = get_object_or_404(Activity, slug=activity_slug)
    paginator = Paginator(item.promot_products.all(), ARTICLE_PAGE_SIZE)
    page = request.GET.get('p')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(paginator.num_pages)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "core/shop_products_base.html", {"item": item, 'page': page, "products": products, "paginator": paginator, 'next': True, 'url': request.get_full_path()})



def shop(request):
    list = []
    brands = Brand.objects.all()
    product_types = ProductType.objects.all()
    return render(request, "core/shop.html", {"brands": brands, "product_types": product_types,  "count": len(list)})

def shop_list(request):
    type_slug = request.GET.get('t')
    brand_slug = request.GET.get('b')
    space_slug = request.GET.get('s')
    page = request.GET.get('p')
    item = None
    if type_slug:
        item = get_object_or_404(ProductType, slug=type_slug)
        paginator = Paginator(item.product_set.all(), ARTICLE_PAGE_SIZE)
    elif brand_slug:
        item = get_object_or_404(Brand, slug=brand_slug)
        paginator = Paginator(item.product_set.all(), ARTICLE_PAGE_SIZE)
    elif space_slug:
        item = get_object_or_404(ProductSpace, slug=space_slug)
        paginator = Paginator(item.applicable_spaces.all(), ARTICLE_PAGE_SIZE)
    else:
        paginator = Paginator(Product.objects.all(), ARTICLE_PAGE_SIZE)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(paginator.num_pages)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "core/shop_products_base.html", {"item": item, 'page': page, "products": products, "paginator": paginator, 'next': True, 'url': request.get_full_path()})

def type(request, type_slug):
    type = get_object_or_404(ProductType, slug=type_slug)
    return render(request, "core/shop_products_base.html", {"item": type, 'title': type.name, 'next': True, 'url': request.get_full_path()})

def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_anonymous():
        is_like = False
    else:
        is_like = product.is_liked_by_user(request.user)
    return render(request, "core/shop_single.html", {"product": product, 'is_like': is_like, 'next': True, 'url': request.get_full_path()})

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, "core/portfolio.html", {"portfolios": portfolios})

def portfolio_info(request, portfolio_slug):
    portfolio_single = get_object_or_404(Portfolio, slug=portfolio_slug)
    if request.user.is_anonymous():
        is_like = False
    else:
        is_like = portfolio_single.is_liked_by_user(request.user)
    return render(request, "core/portfolio_single.html", {"portfolio": portfolio_single, 'is_like': is_like, 'next': True, 'url': request.get_full_path()})

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