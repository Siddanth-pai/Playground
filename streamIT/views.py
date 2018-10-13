from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView#for class based views
from django.http import HttpResponse
# Create your views here.
from .models import Post
#handles the traffic and then returns what user wants to see

#class based views

def home(request):
     context ={
     'posts':Post.objects.all()
     }
     return render(request,'streamIT/home.html',context)#render is a shortcut that helps with passing the request to
     #the render function returns a http HttpResponse
     #our views need to return an http response or exception


class PostListView(ListView):
     model=  Post                         # what model to query  inorder to create list
     template_name = 'streamIT/home.html'# <app>/<model>_<viewtype>.html
     context_object_name = 'posts'#atttribute otherwisewe need to use 'objectlist'
     ordering = ['-date_posted']# for displaying the post from newest to oldest


def about(request):
     return render(request,'streamIT/about.html')
