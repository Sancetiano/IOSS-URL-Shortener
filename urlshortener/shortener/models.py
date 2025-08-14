from django.db import models
from django.contrib.auth.models import User  # Import User

class Url(models.Model):
    long_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow anonymous

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"