"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .import views
#code till video 6
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('harry',views.harry,name='harry'),
    path('youtube',views.Youtube,name='youytube'),
    path('Facebook',views.facebook,name='facebook'),
    path('Whatsapp',views.Whatsappweb,name='Whatsappweb'),
]"""
#code till 9th video
'''urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('removepunc',views.removepunc,name='removepunc'),
    path('capfirst',views.capfirst,name='capfirst'),
    path('spaceremove',views.spaceremove,name='spaceremove'),
    path('newlineremove',views.newlineremove,name='newlineremove'),
    path('charcout',views.charcout,name='charcout'),



    
]'''
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('analyzetxt',views.analyzetxt,name='atext'),
]