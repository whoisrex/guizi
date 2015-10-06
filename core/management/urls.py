from django.conf.urls import url, patterns, include
from tastypie.api import Api
from core.management import views
from core.management.api import PortfolioResource, ProductResource, BrandResource, UserResource, ImageResource, \
    ProductTypeResource, ProductSpaceResource, ArticleResource
from django.conf.urls.static import static

__author__ = 'whoisrex'

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(BrandResource())
v1_api.register(ProductTypeResource())
v1_api.register(ProductSpaceResource())
v1_api.register(ProductResource())
v1_api.register(PortfolioResource())
v1_api.register(ArticleResource())
v1_api.register(ImageResource())

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^api/', include(v1_api.urls)),

)

urlpatterns += static('tpl/', view='django.contrib.staticfiles.views.serve')