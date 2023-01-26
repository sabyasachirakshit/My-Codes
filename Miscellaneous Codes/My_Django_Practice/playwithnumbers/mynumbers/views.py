from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import logics
import pickle
# Create your views here.

universal_user = {"MASTER":"123"}


def check_user_existence(user, passw):
    if user in universal_user.keys():
        if passw == universal_user[user]:
            return "Matched"
        else:
            return "PassNoMatch" 


def home_page(request):
    return render(request, "home_page.html")


def about(request):
    return render(request,"about.html")

def login_page(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username in universal_user:
        return render(request,"user_exist_already.html")
    if username=="" or password =="":
        return render(request,"error.html")
    else:
        universal_user.update({username: password})
        return render(request, "login.html")


def register(request):
    return render(request, "register_user.html")


def user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    condition = check_user_existence(username, password)
    if condition == "Matched":
        return render(request, "home_page.html",{"user":username})
    elif condition == "PassNoMatch":
        return HttpResponse("Passwords do not match!")
    else:
        return HttpResponse("User Does Not Exist!")


def processing(request): 
    html_loc = "result.html"
    start_range_number = int(request.POST.get("min_range", "100"))
    end_range_number = int(request.POST.get("max_range", "1000"))
    armstrong_checkbox = request.POST.get("armstrong", "off")
    disarium_checkbox = request.POST.get("disarium", "off")
    automorphic_checkbox = request.POST.get("automorphic", "off")
    neon_checkbox = request.POST.get("neon", "off")
    sunny_checkbox = request.POST.get("sunny", "off")
    strong_checkbox = request.POST.get("strong", "off")
    trimorphic_checkbox = request.POST.get("trimorphic", "off")
    vampire_checkbox = request.POST.get("vampire", "off")
    if armstrong_checkbox == "on": 
        armstrong_list = logics.check_armstrong(
            start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Armstrong Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": armstrong_list})
    elif disarium_checkbox == "on":
        disarium_list = logics.check_disarium(
            start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Disarium Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": disarium_list})
    elif automorphic_checkbox == "on":
        automorphic_list = logics.check_automorphic(
            start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Automorphic Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": automorphic_list})
    elif neon_checkbox == "on":
        neon_list = logics.check_neon(start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Neon Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": neon_list})
    elif sunny_checkbox == "on":
        sunny_list = logics.check_sunny(start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Sunny Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": sunny_list})
    elif strong_checkbox == "on":
        strong_list = logics.check_strong(start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Strong Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": strong_list})
    elif trimorphic_checkbox == "on":
        trimorphic_list = logics.check_trimorphic(
            start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Trimorphic Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": trimorphic_list})
    elif vampire_checkbox == "on":
        vampire_list = logics.check_vampire(
            start_range_number, end_range_number)
        return render(request, html_loc, {"which_number": "Vampire Number", "min_range": start_range_number, "max_range": end_range_number, "for_loop_iterator": 1, "list": vampire_list})
    else:
        return HttpResponse("Please Check a checkbox!")
