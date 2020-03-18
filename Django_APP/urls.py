"""Django_APP URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from notehub.views import home, register, sign_in, signup_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='notehub'),
    url(r'^register/', register, name='register'),
    url(r'^sign_in/', sign_in, name='sign_in'),
    url(r'^signup/', signup_view, name='signup'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^return/', return_view, name='return'),
    url(r'^notehub/', include('notehub.urls')),
]

urlpatterns += staticfiles_urlpatterns()
