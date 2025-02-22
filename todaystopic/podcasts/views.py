from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.http import HttpResponse
from django.shortcuts import render, redirect

from.models import PodcastChannel, PodcastEpisode, Subscriber

def home(request):
    return render(request, 'podcasts/home.html')

def privacy(request):
    return render(request, 'podcasts/privacy.html')

def terms(request):
    return render(request, 'podcasts/terms.html')

def podcast_page(request):
    channels = PodcastChannel.objects.all().order_by('-pub_date')  # Get all podcasts, ordered by most recent
    return render(request, 'podcasts/podcasts.html', {'channels': channels})

def podcast_episode_detail(request, channel_id, episode_id):
    episode = get_object_or_404(PodcastEpisode, pk=episode_id, channel_id=channel_id)
    context = {'episode': episode}
    return render(request, 'podcasts/episode_detail.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                return redirect('home')
            else:
                return render(request, 'subscription_error.html', {'error': 'You are already subscribed!'})
        except ValidationError:
            return render(request, 'subscription_error.html', {'error': 'Invalid email address.'})
    else:
        return redirect('home')
