"""mysite URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from .views import hello_world,good_bye_world,my_homepage_view,see_time,see_hours_ahead_in_template_view,hours_ahead,see_time_in_shortcutview

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',my_homepage_view),
    url(r'^hello/$',hello_world),
    url(r'^time/$',see_time),
    url(r'^timeshort/$',see_time_in_shortcutview),
    url(r'^hours_ahead/(\d{1,2})/$',hours_ahead),
    url(r'^future_time/(\d{1,3})/$',see_hours_ahead_in_template_view),
    url(r'^goodbye/$',good_bye_world),
]
