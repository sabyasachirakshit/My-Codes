from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns


app_name="tictactoe"

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.homepage)
]