from django.shortcuts import render

# Create your views here.
def calculate(request):
    return render(request,"calculator.html")