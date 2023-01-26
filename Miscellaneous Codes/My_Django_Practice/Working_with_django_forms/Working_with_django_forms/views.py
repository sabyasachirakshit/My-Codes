from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import name_form

def get_name(request):
    if request.method=="POST":
        form=name_form(request.GET)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=name_form()
    return render(request,"name.html",{"forms":form})
        