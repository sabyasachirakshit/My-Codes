from django.http import HttpResponse
def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse('RemovePunc')

def capfirst(request):
    return HttpResponse('capitalize first')

def newlineremove(request):
    return HttpResponse('New line remove')

def spaceremove(request):
    return HttpResponse('SpaceRemove')

def charcount(request):
    return HttpResponse('Charcount')