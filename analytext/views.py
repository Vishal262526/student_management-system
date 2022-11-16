from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req,"index.html")

def analyze(req):
    text = req.POST.get("text","Default")
    removePunc = req.POST.get("removepunc","off")
    capitalize = req.POST.get("capitalize","off")
    uppercase = req.POST.get('uppercase','off')
    lowercase = req.GET.get('lowercase','off')
    newLineRemover = req.POST.get('newlineremover','off')
    spaceremover = req.POST.get("spaceremover",'off')
    analyzed = ""
    
    # Remveve Punchuation
    if removePunc == "on":
        validPunch = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in validPunch:
                analyzed += char 
                text = analyzed

    # Capitalize the text
    if capitalize == "on":
        analyzed = text.capitalize()
        text = analyzed

    # Upcase Text
    if uppercase == "on":
        analyzed = text.upper()
        text = analyzed


    # Lowercase Text
    if lowercase == "on":
        analyzed = text.lower()
        text = analyzed

    # New line Remover
    if newLineRemover == "on":
        for char in text:
            if char != "\n" and char != "\r":
                analyzed += char
        text = analyzed        

    # Space Remover
    if spaceremover == "on":
        for index,char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed += char       
        text = analyzed        
    
    data = {"text":text}
    return render(req,"analyze.html",data)