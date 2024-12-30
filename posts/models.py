from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)  # Rendre unique pour éviter les doublons
    banner = models.ImageField(
        upload_to="post_banners/", default="fallback.jpg", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
