from django.contrib import admin
from .models import PodcastChannel, PodcastEpisode

admin.site.register(PodcastChannel)
admin.site.register(PodcastEpisode)
