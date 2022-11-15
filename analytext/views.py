from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req,"index.html")

def analyze(req):
    text = req.GET.get("text","Default")
    removePunc = req.GET.get("removepunc","off")
    capitalize = req.GET.get("capitalize","off")
    uppercase = req.GET.get('uppercase','off')
    lowercase = req.GET.get('lowercase')
    newLineRemover = req.GET.get('newlineremover')
    analyzed = ""
    
    # Remveve Punchuation
    if removePunc == "on":
        validPunch = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in validPunch:
                analyzed += char 

    # Capitalize the text
    elif capitalize == "on":
        analyzed = text.capitalize()

    # Upcase Text
    elif uppercase == "on":
        analyzed = text.upper()

    # Lowercase Text
    elif lowercase == "on":
        analyzed = text.lower()

    elif newLineRemover == "on":
        pass
    
    data = {"text":analyzed}
    return render(req,"analyze.html",data)