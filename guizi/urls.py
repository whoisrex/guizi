"""guizi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import core.management.urls as API_URL
import core.views as front
from guizi import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/', include(API_URL)),
    url(r'^user/', include('userena.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^$', front.home, name="title"),
    url(r'^uploads/', front.uploads),
    url(r'^shop/$', front.shop),
    url(r'^shop/list/$', front.shop_list),
    # url(r'^shop/type/(?P<type_slug>[^/]+)/$', front.type),
    # url(r'^shop/brand/(?P<brand_slug>[^/]+)/$', front.brand),
    url(r'^shop/(?P<product_id>\d+)$', front.product_info),
    url(r'^portfolio/$', front.portfolio),
    url(r'^portfolio/(?P<portfolio_slug>[^/]+)/$', front.portfolio_info),
    url(r'^article/$', front.blog),
    url(r'^article/(?P<article_slug>[^/]+)/$', front.article_info),
    url(r'like/', front.like),
    url(r'about-us/', front.aboutus, name="find-us"),
    url(r'find-us/', front.contact),
    url(r'^search/', include('haystack.urls')),
]

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
