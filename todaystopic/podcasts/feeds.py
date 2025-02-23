import uuid

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils import timezone
from django.urls import reverse

from.models import PodcastChannel, PodcastEpisode

class PodcastFeed(Feed):
    INVALID = 'INVALID'

    feed_type = Rss201rev2Feed

    def get_object(self, request):
        try:
            return PodcastChannel.objects.first()
        except PodcastChannel.DoesNotExist:
            return HttpResponse(
                """
                <?xml version="1.0" encoding="UTF-8"?>
                <rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
                  <channel>
                    <title>No Episodes Yet</title>
                    <link>https://www.example.com</link>  
                    <description>This podcast channel doesn't have any episodes yet. Stay tuned!</description>
                  </channel>
                </rss>
                """,
                content_type='application/rss+xml'
            )


    # number 2
    def title(self, obj):
        if obj:
            return obj.title
        return self.INVALID
    # number 3
    def description(self, obj):
        if obj:
            return obj.description
        return self.INVALID

    # syndication checks link first
    def link(self, obj):
        if obj:
            return obj.link
        return 'http://example.com'

    def managing_editor(self, obj):
        if obj:
            return obj.managing_editor
        return self.INVALID

    def web_master(self, obj):
        if obj:
            return obj.web_master
        return self.INVALID

    def language(self, obj):
        if obj:
            return obj.language
        return self.INVALID
    
    def copyright(self, obj):
        return obj.copyright_info

    def feed_url(self, obj):
        if obj and obj.link:
            return obj.link + '/podcasts/rss/'
        return 'https://www.example.com/podcasts/rss/'

    def pub_date(self,obj):
        if obj:
            return obj.pub_date
        return timezone.now()

    def image(self, obj):
        if obj.artwork:
            return obj.artwork.url
        return self.INVALID

    def feed_extra_kwargs(self, obj):
        extra_kwargs = super().feed_extra_kwargs(obj)
        if obj:
            extra_kwargs['itunes_owner'] = {
                'itunes_name': obj.owner_name,
                'itunes_email': obj.owner_email,
            }
            
            extra_kwargs['itunes_author'] = obj.author
            extra_kwargs['itunes_image'] = obj.image.url
            extra_kwargs['itunes_category'] = [{'text': obj.category}]
            extra_kwargs['itunes_explicit'] = obj.explicit
        return extra_kwargs
    
    def items(self, obj):
        if obj:
            episodes = PodcastEpisode.objects.filter(channel=obj).order_by('-pub_date')
        else:
            episodes = PodcastEpisode.objects.all().order_by('pub_date')

        if episodes:
            return episodes
        else:
            # Create a default PodcastEpisode object
            default_episode = PodcastEpisode(
                title="No Episodes Yet",
                description="This podcast channel doesn't have any episodes yet. Stay tuned!",
                link=obj.link if obj else "https://www.example.com",  # Use channel link or default
                guid=uuid.uuid4(),
                pub_date=timezone.now(),
                # Add other necessary fields with default values if needed
            )
            return [default_episode]

    def item_title(self, item):
        if item:
            return item.title
        return self.INVALID

    def item_description(self, item):
        if item:
            return item.description
        return self.INVALID

    def item_description(self, item):
        if item:
            return item.description
        return self.INVALID
    def item_link(self, item):
        if item:
            return item.link
        return self.INVALID

    def item_guid(self, item):
        if item:
            return str(item.guid)
        return self.INVALID
    
    def item_pubdate(self, item):
        if item:
            return item.pub_date
        return self.INVALID

    def item_enclosure_length(self, item):
        if item:
            return item.file_length
        return self.INVALID

    def item_enclosure_mime_type(self, item):
        if item:
            return item.file_type
        return self.INVALID

    def item_enclosure_url(self, item):
        if item.file and item.file.url:
            return self.request.build_absolute_uri(item.file.url)
        return self.INVALID
