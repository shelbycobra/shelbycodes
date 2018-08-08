from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'^blog/blog/view/(?P<slug>[^\.]+).html', views.view_category, name="view_blog_category"),
    path(r'^blog/blog/view/(?P<slug>[^\.]+).html', views.view_post, name="view_blog_post")
]