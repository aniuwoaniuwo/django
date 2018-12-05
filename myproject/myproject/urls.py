"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.conf.urls import url
from database import views as database_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',database_views.index,name='index'),
    url(r'^classifications/(?P<classification_slug>[^/]+)/$',database_views.classindex,name='classifications'),
    url(r'^data/(?P<data_slug>[^/]+)/$',database_views.dataindex,name='data')#最后形成的网址是data/+[]里面的参数，<>id，id传到views，这样的好处是（）的不管怎么变化都可以根据id传过去
]

#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
