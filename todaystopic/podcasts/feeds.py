from django.contrib.syndication.views import Feed
from django.urls import reverse

from.models import Podcast

class PodcastFeed(Feed):
    title = "Today's Topic"  # Replace with your podcast title
    link = "/podcast.rss"  # The URL for your RSS feed
    d_intro = "Listen to Barnaby Badgers and Mad Max McBarker talk about stuff."
    d_tag = "Sometimes it's interesting. Sometimes it's got bite but it's always something." 
    d_conclusion = "Subscribe now and find out what."
    description = f"{d_intro} {d_tag} {d_conclusion}"

    def items(self):
        return Podcast.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        # Absolute URL for episode if available, else relative URL
        if item.link:
            return item.link
        else:
            return f"/episode/{item.id}"  # Example relative URL

    def item_pubdate(self, item):
        return item.pub_date

    def item_enclosure_url(self, item):
        return item.enclosure_url

    def item_enclosure_length(self, item):
        return item.enclosure_length

    def item_enclosure_mime_type(self, item):
        return item.enclosure_type

    def item_guid(self, item):
        return item.guid

    def item_itunes_duration(self, item):
        return item.duration

    def item_image(self, item):
        if item.image:
            return item.image.url
        return None

    # Channel-level data (using property to avoid repeated queries):
    @property
    def podcast_data(self):
        try:
            return Podcast.objects.all().first()  # Get the first podcast for channel info
        except Podcast.DoesNotExist:
            return None

    def title(self): # Overriding the basic title
        podcast = self.podcast_data
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
