from django.contrib import admin
from .models import TrendingHashtags

@admin.register(TrendingHashtags)
class TrendingHashtagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'trend1', 'trend2', 'trend3', 'trend4', 'created_at')
