from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render

 

from django.http.response import Http404

def my_homepage_view(request):
    return HttpResponse("<html><body>This is My Homepage View! Welcome To my first ever Django Project. <br> If you want to see hello world- go to url: hello. <br> If you want to see good bye page- go to url: goodbye. <br> If you want to check time- go to url: timeshort <br> If you want to check time ahead of certain hour go to url : future_time/(hours mentioned)/ <br>Thank You </body></html>")

def hello_world(request):
    return HttpResponse("Hello World!!")

def good_bye_world(request):
    return HttpResponse("GoodBye! Have a Nice Day!!")

def see_time(request):
    now=datetime.now()
    t=Template("It is now {{ current_datetime }}")
    html=t.render(Context({'current_datetime':now}))
    return HttpResponse(html)

def see_time_in_shortcutview(request):
    now=datetime.now()
    return render(request, 'see_time.html',{'current_datetime':now})

def see_hours_ahead_in_template_view(request,offset):
    try:
        offset=int(offset)
    except Http404:
        raise Http404()
    ahead_time=datetime.now()+timedelta(hours=offset)
    return render(request, 'future_time.html', {'hour_offset':offset,'next_time':ahead_time})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except Http404:
        raise Http404()
    future_time=datetime.now()+timedelta(hours=offset)
    return HttpResponse(f"The time after {offset} hours ahead would be:{future_time}")
