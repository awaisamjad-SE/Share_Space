from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="A catchy title for your post")
    text = models.TextField(max_length=280, help_text="Main content of your post")
    description = models.TextField(max_length=1000, blank=True, null=True, help_text="Detailed description (optional)")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_private = models.BooleanField(default=False)  # True = Private, False = Public
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        privacy = "Private" if self.is_private else "Public"
        return f"{self.user.username} - {self.title} ({privacy})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tweet:tweet_detail', kwargs={'tweet_id': self.id})
