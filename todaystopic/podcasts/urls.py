from django.urls import path
from . import views
from .feeds import PodcastFeed

urlpatterns = [
    path("", views.home, name="home"),
    path('podcasts/', views.podcast_page, name='podcasts'),
    path('feed/<int:channel_id>/', PodcastFeed(), name='podcast_feed'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
