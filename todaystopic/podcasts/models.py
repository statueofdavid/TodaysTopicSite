from django.db import models
from django.utils import timezone
import uuid

class Podcast(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the podcast episode")
    description = models.TextField(help_text="Detailed description of the episode")
    link = models.URLField(blank=True, null=True, help_text="Link to the episode (e.g. on another platform)")
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, help_text="Globally Unique Identifier")
    pub_date = models.DateTimeField(default=timezone.now, help_text="Date and time the episode was published")
    enclosure_url = models.URLField(max_length=255, help_text="URL of the audio file")
    enclosure_length = models.IntegerField(blank=True, null=True, help_text="Length of the audio file in bytes")
    enclosure_type = models.CharField(max_length=50, default="audio/mpeg", help_text="Content type of the audio file")
    duration = models.CharField(max_length=20, blank=True, null=True, help_text="Duration of the audio (e.g., '1:30:00')")
    explicit = models.BooleanField(default=False, help_text="Is the content explicit?")
    image = models.ImageField(upload_to='podcast_images/', blank=True, null=True, help_text="Episode artwork")

    # Channel-level fields (maybe a separate PodcastChannel model ***FUTURE_SELF***)
    podcast_title = models.CharField(max_length=255, help_text="Title of the podcast channel (e.g., 'David\'s Declared Space')")
    podcast_description = models.TextField(help_text="Description of the podcast channel")
    podcast_link = models.URLField(help_text="Link to the podcast channel")
    managing_editor = models.EmailField(blank=True, null=True, help_text="Managing editor email")
    web_master = models.EmailField(blank=True, null=True, help_text="Web master email")
    language = models.CharField(max_length=10, default="en-us", help_text="Language of the podcast (e.g., 'en-us')")
    copyright_info = models.CharField(max_length=255, blank=True, null=True, help_text="Copyright information")
    itunes_author = models.CharField(max_length=255, blank=True, null=True, help_text="iTunes author")
    itunes_owner_name = models.CharField(max_length=255, blank=True, null=True, help_text="iTunes owner name")
    itunes_owner_email = models.EmailField(blank=True, null=True, help_text="iTunes owner email")
    itunes_image = models.ImageField(upload_to='podcast_channel_images/', blank=True, null=True, help_text="iTunes channel artwork")
    itunes_category = models.CharField(max_length=255, blank=True, null=True, help_text="iTunes category")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if self.audio_file:
            try:
                self.enclosure_length = self.audio_file.size
            except Exception as e:
                print(f"Error getting file size: {e}")
        super().save(*args, **kwargs)
