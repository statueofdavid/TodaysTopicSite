from django.urls import path
from . import views
from .feeds import PodcastFeed
from .views import podcast_episode_detail

urlpatterns = [
    path("", views.home, name="home"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('podcasts/', views.podcast_page, name='podcasts'),
    path('podcasts/<int:channel_id>/<int:episode_id>/',podcast_episode_detail,name='podcast_episode_detail'),
    path('podcasts/rss/', PodcastFeed(), name='podcast_feed'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
