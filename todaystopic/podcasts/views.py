from django.shortcuts import render
from django.http import HttpResponse
from.models import PodcastChannel, PodcastEpisode

def podcast_page(request):
    podcasts = PodcastChannel.objects.all().order_by('-pub_date')  # Get all podcasts, ordered by most recent
    return render(request, 'podcasts/podcasts.html', {'podcasts': podcasts})

def home(request):
    return render(request, 'podcasts/home.html')
