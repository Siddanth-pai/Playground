
from django.urls import path
#from django.urls import url

from .views import PostListView
from . import views
from .models import Post
from users import views as user_views

urlpatterns = [
    path('',PostListView.as_view(),name='vlog-home'),#home path.....it searches for home functions in views.py.....http://127.0.0.1:8000/streamIT/
    #path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),#for displaying individual_post.........
    #path('post/(?P<pk>\d+)/',PostDetailView.as_view(), name='post-detail'),
    #path('post/<int:pk>/',views.post_detail, name='post_detail'),
    #path('about/',views.about,name='vlog-about'),#http://127.0.0.1:8000/streamIT/about/
    path('videos/',user_views.showvideo,name = 'showvideo'),
    path('audi/',user_views.showaudio,name = 'showaudio'),

    #path('videos/',)
]
