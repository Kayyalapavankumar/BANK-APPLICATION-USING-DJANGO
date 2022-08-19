"""bank1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ATM import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^register/', views.register),
    url(r'^online/', views.online),
    url(r'^back/', views.back),
    url(r'^login/', views.login),
    url(r'^deposit/', views.pindeposit),
    url(r'^pindeposit/', views.deposit),
    url(r'^withdraw/', views.pinwithdraw),
    url(r'^balance/', views.pinbalance),
    url(r'^pinwithdraw/', views.withdraw),
    url(r'^pinbalance/', views.balance),
    url(r'^pinchange/', views.pinchange),
    url(r'^newpin/', views.newpin),
    url(r'^newpinchange/',views.newpinchange),
    url(r'^successful/', views.successful_registration),
    url(r'^success_deposit/', views.successful_deposit),
    url(r'^success_withdraw/', views.successful_withdraw),
]
