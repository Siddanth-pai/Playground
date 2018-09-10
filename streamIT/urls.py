
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='vlog-home'),#home path.....it searches for home functions in views.py.....http://127.0.0.1:8000/streamIT/
    path('about/',views.about,name='vlog-about'),#http://127.0.0.1:8000/streamIT/about/ 
]
