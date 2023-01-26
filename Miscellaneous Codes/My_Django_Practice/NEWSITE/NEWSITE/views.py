from django.shortcuts import render

def my_home_page(request):
    return render(request,"home_base.html")