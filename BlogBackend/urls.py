"""BlogBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from BlogBackend.custom_site import cus_site
from apps.weblog.views import IndexView, PostDetailView, CategoryView, TagView, links

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<pk>\d+).html/$', PostDetailView.as_view(), name='post-detail'),
    re_path(r'^links/$', links, name='links'),

    re_path('^superAdmin/', admin.site.urls, name='super-admin'),
    re_path('^admin/', cus_site.urls, name='admin'),
]
