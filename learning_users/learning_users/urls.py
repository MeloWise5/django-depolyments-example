"""learning_users URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from basic_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #include allows us to use a different URLS page to find the redirect
    #you know its being used when the template link uses {% url 'basic_app:'%}
    #that link tells this page to send the 'basic_app:login' ":login" data to the app/urls.py
    #we can use the --basic_app-- name because we established in it the app/urls.py file
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'^admin/', admin.site.urls),
    #name=logout is the name you use when linking to this URL redirect
    #it then looks into the apps/views.py file for user_logout function
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special'),
]
