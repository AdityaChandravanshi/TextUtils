#I have created this file - Aditya
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

def analiyzed(request):
    #Get the text

    text=request.POST.get('text', 'default')

    #Check checkbox value

    removepunc=request.POST.get('removepunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    lowercase=request.POST.get('uppercase', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    # charactercount=request.GET.get('charactercount', 'off')
    # print(removepunc)
    # print(text)

    #check which checkbox is on

    if removepunc == "on":
    #analiyzed=text
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
        analiyzed=""
        for char in text:
            if char not in punctuations:
                analiyzed = analiyzed + char
        params={'purpose':'Removed Punctuation','analiyzed_text':analiyzed}
        text = analiyzed
        # return render(request,'analiyzed.html',params)
        
    if uppercase == "on":
        analiyzed=""
        for char in text:
            analiyzed = analiyzed + char.upper()
        params={'purpose':'Changed to Uppercase','analiyzed_text':analiyzed}
        text = analiyzed
        # return render(request,'analiyzed.html',params)
    

    if newlineremover == "on":
        analiyzed=""
        for char in text:
            if char != "\n" and char != "\r":
                analiyzed = analiyzed + char
        params={'purpose':'Removed New Lines','analiyzed_text':analiyzed}
        return render(request,'analiyzed.html',params)
    
    if extraspaceremover == "on":
        analiyzed=""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analiyzed = analiyzed + char
        params={'purpose':'Removed New Lines','analiyzed_text':analiyzed}

    if(removepunc != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select the any operation and try again")

        # text = analiyzed
        # return render(request,'analiyzed.html',params)
    # else:
    #     return HttpResponse("Error")
    
    return render(request,'analiyzed.html',params)