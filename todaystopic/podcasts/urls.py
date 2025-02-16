from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('podcasts/', views.podcast_page, name='podcasts'),  # Example URL: /podcasts/
]
