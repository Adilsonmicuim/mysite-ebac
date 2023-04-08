from django.urls import path

from blog import views



urlpatters = [
    path('', views.PostView.as_view(), name='home'),
    # path('test_post_view', test_post_view, name='home'),
]
