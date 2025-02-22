import uuid

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import *
from django.utils import timezone
from django.urls import reverse

from.models import PodcastChannel, PodcastEpisode, Subscriber

class PodcastFeed(Feed):
    title = "Today's Topic"  # Replace with your podcast title
    link = "/podcast.rss"  # The URL for your RSS feed
    d_intro = "Listen to Barnaby Badgers and Mad Max McBarker talk about stuff."
    d_tag = "Sometimes it's interesting. Sometimes it's got bite but it's always something." 
    d_conclusion = "Subscribe now and find out what."
    description = f"{d_intro} {d_tag} {d_conclusion}"

    @property
    def podcastChannel(self):
        try:
            return PodcastChannel.objects.all().first()
        except PodcastChannel.DoesNotExist:
            return None
            
    def domain(self, obj):
        return 'declared.space'
    
    def items(self, obj):
        episodes = PodcastEpisode.objects.all().order_by('-pub_date')
        
        if episodes:
            return episodes
        else:
            return [PodcastEpisode(
                title="No Episodes Yet",
                description="This podcast channel doesn't have any episodes yet. Stay tuned!",
                guid=uuid.uuid4(), 
                pub_date=timezone.now(),
            )]

    def title(self):
        podcast = self.podcastChannel
        return podcast.podcast_title if podcast else "Your Podcast Title"

    def description(self): # Overriding the basic description
        podcast = self.podcastChannel
        return podcast.podcast_description if podcast else "Your podcast description"

    def link(self): # Overriding the basic link
        podcast = self.podcastChannel
        return podcast.podcast_link if podcast else "/rss"

    def managing_editor(self):
        podcast = self.podcastChanel
        return podcast.managing_editor if podcast else None

    def web_master(self):
        podcast = self.podcastChannel
        return podcast.web_master if podcast else None

    def language(self):
        podcast = self.podcastChannel
        return podcast.language if podcast else "en-us"

    def copyright(self):
        podcast = self.podcastChannel
        return podcast.copyright if podcast else None

    def itunes_author(self):
        podcast = self.podcastChannel
        return podcast.itunes_author if podcast else None

    def itunes_owner_name(self):
        podcast = self.podcastChannel
        return podcast.itunes_owner_name if podcast else None

    def itunes_owner_email(self):
        podcast = self.podcastChannel
        return podcast.itunes_owner_email if podcast else None

    def itunes_image(self):
        podcast = self.podcastChannel
        return podcast.itunes_image.url if podcast and podcast.itunes_image else None

    def itunes_category(self):
        podcast = self.podcastChannel
        return podcast.itunes_category if podcast else None

    def item_author_name(self, item):
        try:
            return item.channel.author
        except PodcastEpisode.channel.RelatedObjectDoesNotExist:
            return None

    def item_enclosure_url(self, item):
        if item.file and item.file.url:
            return self.request.build_absolute_uri(item.file.url)
        return None

    def item_link(self, item):
        try:
            return reverse('podcast_episode_detail', args=[item.channel.id, item.id])
        except PodcastEpisode.channel.RelatedObjectDoesNotExist:
            return None