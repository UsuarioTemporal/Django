from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request,*args,**kwargs):
    return HttpResponse("<h1>Hello world</h1>")

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})
    