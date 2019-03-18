from django.conf.urls import include, url

from django.contrib import admin
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'snippets', views.SnippetView)

urlpatterns = [#[url(r'^', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]
