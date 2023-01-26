from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name="appname"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
]