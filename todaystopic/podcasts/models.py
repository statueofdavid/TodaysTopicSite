from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.urls import reverse
from.models import PodcastChannel, PodcastEpisode

class PodcastFeed(Feed):
    feed_type = Rss201rev2Feed

    def get_object(self, request, channel_id):
        return PodcastChannel.objects.get(pk=channel_id)

    def title(self, obj):
        return obj.title

    def link(self, obj):
        return obj.link

    def description(self, obj):
        return obj.description

    def managing_editor(self, obj):
        return obj.managing_editor

    def web_master(self, obj):
        return obj.web_master

    def copyright(self, obj):
        return obj.copyright_info

    def author_name(self, obj):
        return obj.author

    def feed_url(self, obj):
        return reverse('podcast_feed', args=[obj.id])

    def image(self, obj):
        return obj.artwork.url if obj.artwork else None

    def language(self, obj):
        return 'en-us'

    def categories(self, obj):
        return [obj.category]

    def items(self, obj):
        return PodcastEpisode.objects.filter(channel=obj).order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.link

    def item_enclosure_url(self, item):
        if item.file and item.file.url:
            return self.request.build_absolute_uri(item.file.url)
        return None

    def item_enclosure_length(self, item):
        return item.file_length

    def item_enclosure_mime_type(self, item):
        return item.file_type

    def item_pubdate(self, item):
        return item.pub_date

    def item_guid(self, item):
        return str(item.guid)

    def item_author_name(self, item):
        return item.channel.author

    def item_explicit(self, item):
        return item.explicit