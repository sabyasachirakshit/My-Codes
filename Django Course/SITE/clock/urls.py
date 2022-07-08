from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name="clock"

urlpatterns=[
    path('admin/', admin.site.urls),
    path(r'',views.home_page),
    path(r'check_time',views.clock),
]