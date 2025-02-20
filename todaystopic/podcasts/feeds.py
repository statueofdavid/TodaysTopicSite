from django.contrib.syndication.views import Feed
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
            return PodcastChannel.objects.all().first()  # Get the first podcast for channel info
        except PodcastChannel.DoesNotExist:
            return None

    def title(self):
        podcast = self.podcastChannel
        return podcast.podcast_title if podcast else "Your Podcast Title"

    def description(self): # Overriding the basic description
        podcast = self.podcast_data
        return podcast.podcast_description if podcast else "Your podcast description"

    def link(self): # Overriding the basic link
        podcast = self.podcast_data
        return podcast.podcast_link if podcast else "/podcast.rss"

    def managing_editor(self):
        podcast = self.podcast_data
        return podcast.managing_editor if podcast else None

    def web_master(self):
        podcast = self.podcast_data
        return podcast.web_master if podcast else None

    def language(self):
        podcast = self.podcast_data
        return podcast.language if podcast else "en-us"

    def copyright(self):
        podcast = self.podcast_data
        return podcast.copyright if podcast else None

    def itunes_author(self):
        podcast = self.podcast_data
        return podcast.itunes_author if podcast else None

    def itunes_owner_name(self):
        podcast = self.podcast_data
        return podcast.itunes_owner_name if podcast else None

    def itunes_owner_email(self):
        podcast = self.podcast_data
        return podcast.itunes_owner_email if podcast else None

    def itunes_image(self):
        podcast = self.podcast_data
        return podcast.itunes_image.url if podcast and podcast.itunes_image else None

    def itunes_category(self):
        podcast = self.podcast_data
        return podcast.itunes_category if podcast else None
