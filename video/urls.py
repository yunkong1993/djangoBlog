from django.urls import path
from . import views

app_name = 'video'
urlpatterns = [

    path('video', views.VideoView.as_view(), name='video'),
    path('video/detail/', views.detail, name='detail'),
    path('video/search/', views.search, name='search'),
    path('video/play/', views.play, name='play'),
]
