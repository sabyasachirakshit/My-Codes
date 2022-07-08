from django.shortcuts import render

# Create your views here.

def homepage(request):
    var1=request.POST.get('option1_outlined')
    var2=request.POST.get('option2-outlined')
    params={
        'var1':var1,
        'var2':var2,
    }
    return render(request,"base.html",params)
 