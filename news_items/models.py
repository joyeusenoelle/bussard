from django.db import models


class NewsSource(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.CharField(max_length=255)
    rss_url = models.CharField(max_length=255)
    created_at = models.DateTimeField("Date added to database")
    updated_at = models.DateTimeField("Last time the feed was checked")

    def __str__(self) -> str:
        return f"{self.name}: {self.url[:50]}"


class NewsItem(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=False, blank=False)
    date_posted = models.DateTimeField("Date posted to the remote feed")
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.source.name}: {self.title} ({self.date_posted})"
