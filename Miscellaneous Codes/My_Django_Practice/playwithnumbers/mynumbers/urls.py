from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns
from . import views
app_name="mynumbers"

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.login_page), 
    path('login',views.login_page),
    path('about',views.about),
    path('home_page',views.home_page),
    path('check_if_user_exists',views.user),
    path('process',views.processing),
    path('register_user',views.register),
]