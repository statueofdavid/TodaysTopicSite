# Generated by Django 5.1.6 on 2025-02-18 03:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0005_podcastchannel_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('email', models.EmailField(max_length=254, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
