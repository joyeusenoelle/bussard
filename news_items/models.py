from django.db import models


class NewsSource(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.CharField(max_length=255)
    rss_url = models.CharField(max_length=255)
    created_at = models.DateTimeField("Date added to database")
    updated_at = models.DateTimeField("Last time the feed was checked")


class NewsItem(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=False, blank=False)
    date_posted = models.DateTimeField("Date posted to the remote feed")
    seen = models.BooleanField(default=False)
