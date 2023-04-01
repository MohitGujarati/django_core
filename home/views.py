from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hey this is Django server")


def html_page(request):
   return  render (request,"index.html")

def CanVote(request):
    
    peoples = [
        {'name':'Mohit','background':'Computer Eng','age':'21'},
        {'name':'Mohit','background':'Computer Eng','age':'16'},
        {'name':'Mohit','background':'Computer Eng','age':'29'},
        {'name':'Mohit','background':'Computer Eng','age':'17'}
    ]
    
    return render (request,"canvote.html",context={'peoples':peoples})