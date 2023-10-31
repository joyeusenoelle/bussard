from django.contrib import admin

from .models import NewsItem, NewsSource

admin.site.register(NewsSource)
admin.site.register(NewsItem)
