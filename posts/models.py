from django.db import models
from django.contrib.auth.models import AbstractUser
import scrap_post.settings as scrapsettings
from django.urls import reverse


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

CITIES = (
    (0, "Raleigh"),
    (1, "Durham"),
    (2, "Cary"),
    (3, "Morrisville"),
    (4, "Apex"),
    (5, "Garner"),
)

Flags = (
    (0, 'saved'),
    (0, 'report'),
)


class ScrapUser(AbstractUser):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'ScrapUser'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)
    city_name = models.IntegerField(choices=CITIES, default=0)
    author = models.ForeignKey(scrapsettings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post')
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    phone_number = models.CharField(max_length=200, default='')
    email_address = models.CharField(max_length=200, default='')
    saved = models.ManyToManyField(ScrapUser, null=True, related_name='add_saved')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('posts:index')




