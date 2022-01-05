from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ShortedLink(models.Model):
    orig_url = models.URLField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'user: {self.creator.username}, original link: {self.orig_url}'

    def get_absolute_url(self):
        return reverse('resolve-link', kwargs={'identifier': self.short_url})
