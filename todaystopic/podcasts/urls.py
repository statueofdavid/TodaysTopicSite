from django.urls import path
from . import views, feeds

urlpatterns = [
    path("", views.home, name="home"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('podcasts/', views.podcast_page, name='podcasts'),
    path('podcasts/rss/', feeds.PodcastFeed(), name='podcast_feed'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
