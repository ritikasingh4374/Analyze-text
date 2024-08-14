#i have created this file
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def navigate(request):
    return render(request, 'navigate.html')

def analyze(request):
    djtext = (request.GET.get('text','default'))
    remove = (request.GET.get('removepunc','off'))
    removenew = (request.GET.get('removenew','off'))
    allcap = (request.GET.get('allcap','off'))
    removespace = (request.GET.get('removespace','off'))
    print(djtext)
    print(remove)
    print(allcap)
    if remove == "on":
        punctuations = '''@#$%%^^&&**(){}[]'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed += char
            

        params = {'purpose': 'Removed punctuations', 'analysed_text' : analysed}
        return render(request, 'analyze.html', params)
    
    if allcap == "on":
        analysed = ""
        for char in djtext:
            analysed += char.upper()
            

        params = {'purpose': 'capitalised', 'analysed_text' : analysed}
        return render(request, 'analyze.html', params)
    
    if removenew == "on":
        analysed = ""
        for char in djtext:
            if char!= "\n":
                analysed += char
            

        params = {'purpose': 'removenew', 'analysed_text' : analysed}
        return render(request, 'analyze.html', params)
    
    if removespace == "on":
        analysed = ""
        for char in djtext:
            if char!= ' ':
                analysed += char
            

        params = {'purpose': 'removespace', 'analysed_text' : analysed}
        return render(request, 'analyze.html', params)
    
    else :
        return HttpResponse("error")
