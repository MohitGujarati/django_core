from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hey this is Django server")


def html_page(request):
   return  render (request,"index.html")

def about_page(request):
   return  render (request,"about.html")

def contacts_page(request):
   return  render (request,"contacts.html")

def CanVote(request):
    
    peoples = [
        {'name':'Mohit','background':'Computer Eng','age':24},
        {'name':'Kunal','background':'Computer Eng','age':17},
        {'name':'Mihir','background':'Computer Eng','age':16},
        {'name':'yashvi','background':'Computer Eng','age':23}
    ]
    
    Text="""
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
    """
    vegetables = ['Carrots', 'Broccoli', 'Cauliflower', 'Spinach', 'Cabbage', 'Bell peppers', 'Tomatoes', 'Onions']

    return render (request,"canvote.html",context={'peoples':peoples,'text':Text, 'vegetables':vegetables})