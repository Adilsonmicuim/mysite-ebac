from django.urls import path

from blog.views import Post

urlpatterns = [
    path('home', Post, name='home'),
]
