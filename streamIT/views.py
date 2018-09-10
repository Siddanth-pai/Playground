from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
  {
     'author' :'Siddanth',
     'title':'Blog Post 1',
     'content': 'First post content',
     'date_posted':'August,2018',
  },
  {
     'author' :'Sid',
     'title':'Blog Post 2',
     'content':'Secondt post content',
     'date_posted':'August,2018'
  },
]
#handles the traffic and then returns what user wants to see

def home(request):
     context ={
     'posts':posts
     }
     return render(request,'streamIT/home.html',context)#render is a shortcut that helps with passing the request to
     #the render function returns a http HttpResponse
     #our views need to return an http response or exception


def about(request):
     return render(request,'streamIT/about.html')
