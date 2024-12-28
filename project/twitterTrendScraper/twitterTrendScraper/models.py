from django.db import models

class TrendingHashtags(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    trend1 = models.CharField(max_length=255, blank=True, null=True)  # First trend
    trend2 = models.CharField(max_length=255, blank=True, null=True)  # Second trend
    trend3 = models.CharField(max_length=255, blank=True, null=True)  # Third trend
    trend4 = models.CharField(max_length=255, blank=True, null=True)  # Fourth trend
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the record was created

    def __str__(self):
        return f"TrendingHashtags {self.id}"
