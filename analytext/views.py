from django.http import HttpResponse


def index(req):
    return HttpResponse("Home")

def about(req):
    return HttpResponse("About")    