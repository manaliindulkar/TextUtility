
from django.http import HttpResponse

from django.shortcuts import render
def index(request):
     return render(request,'index.html')


def analyze(request):
    d=request.POST.get('text','default')
    re=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    print(re)
    #analyzed=d

    if re=="on":
     punctuations='''!()-[]{};:"'\,<>./?@#$%^&*_~'''
     analyzed=""
     for char in d:
        if char not in punctuations:
            analyzed=analyzed+char
     params={'purpose':'removed punctuations','analyzed_text':analyzed}
     d=analyzed

     #return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in d:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'chnaged to uppercase', 'analyzed_text': analyzed}
        d=analyzed

        #return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in d:
            if char!="\n" and char!="\r":

             analyzed=analyzed+char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        d=analyzed

       # return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(d):

            if  (d[index]==" "and d[index+1]==" "):
                pass
            else:

               analyzed=analyzed+char


        params = {'purpose': 'removed extra space', 'analyzed_text': analyzed}
        d=analyzed

        #return render(request, 'analyze.html', params)
    if charactercounter=="on":

        count=0
        for char in d:

            if char!=" ":
                count+=1
        analyzed=count


        params = {'purpose': 'Count character', 'analyzed_text': analyzed}
        d=analyzed
    if (re!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charactercounter!="on"):
        return HttpResponse("select operation")


    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'About.html')













