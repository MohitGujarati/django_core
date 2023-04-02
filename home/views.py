from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hey this is Django server")


def html_page(request):
   return  render (request,"index.html")

def CanVote(request):
    
    peoples = [
        {'name':'Mohit','background':'Computer Eng','age':24},
        {'name':'Kunal','background':'Computer Eng','age':17},
        {'name':'Mihir','background':'Computer Eng','age':16},
        {'name':'yashvi','background':'Computer Eng','age':23}
    ]
    
    return render (request,"canvote.html",context={'peoples':peoples})