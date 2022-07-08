from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def removepunc(request):
    #Get The Text
    djtext=(request.GET.get('text','default'))
    print(djtext)
    #Analyze The Text 
    return HttpResponse('RemovePunc')

def analyze(request):
    #Get The Text
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    spaceremover=(request.POST.get('spaceremover','off'))
    charcount=(request.POST.get('charcount','off'))
    print(removepunc)
    print(djtext)
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        #Analyze The Text
        return render(request,'analyze.html',params)
    elif fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        #Analyze The Text
        return render(request,'analyze.html',params)
    elif newlineremover=='on':
        analyzed="" 
        for char in djtext:
            if char!='\n':
                analyzed=analyzed+char
        params={'purpose':'Removed New Lines','analyzed_text':analyzed}
        #Analyze The Text
        return render(request,'analyze.html',params)
    elif spaceremover=='on':
        analyzed=""
        for char in djtext:
            if char!=' ':
                analyzed=analyzed+char
        params={'purpose':'Removed Spaces','analyzed_text':analyzed}
        #Analyze The Text
        return render(request,'analyze.html',params)
    elif charcount=='on':
        analyzed=0
        for char in djtext:
            analyzed+=1
        params={'purpose':'No. of Characters','analyzed_text':analyzed}
        #Analyze The Text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')


def capfirst(request):
    return HttpResponse('capitalize first')

def newlineremove(request):
    return HttpResponse('New line remove')

def spaceremove(request):
    return HttpResponse('SpaceRemove')

def charcount(request):
    return HttpResponse('Charcount')