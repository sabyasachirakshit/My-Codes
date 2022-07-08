from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'cse'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.about, name="index"),
    path('about/',views.about, name="about"),
    path('test/',views.test, name="test"),

]