#I Have Created This File
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hello Sabyasachi</h1>")
def about(request):
    return HttpResponse("<h1>About Sabyasachi</h1>")