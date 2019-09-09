"""myproject URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# myproject/myproject/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from Share.views import HomeView,Displayiew,MyView,SearchView #导入 视图函数中的对象

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name="home"), #引用视图对象需要调用对象的as_view(),
    #因为是以对象的形式去调用视图,必须要加括号,而不是 as_view。
	
	url(r'^s/(?P<code>\d+)/$',DisplayView.as_view()),
    #/s/(?P<code>\d+ 使用了组匹配的方式 匹配code任意长度的数字，如/s/123456,将123456传给 DisplayView,这里的 code 必须和视图函数的 code 保持一致.
	
	url(r'^my/$',MyView.as_view(),name="MY"), #这里我们添加 MyView,并起名为 MY
	
	url(r'^search/',SearchView.as_view(),name="search"), #添加的路由
]
