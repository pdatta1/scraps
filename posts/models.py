from django.db import models
from django.contrib.auth.models import AbstractUser
import scrap_post.settings as scrapsettings


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


class ScrapUser(AbstractUser):
    post = models.ForeignKey('Post', null=True, on_delete=models.CASCADE)

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

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.slug

    def get_city_name(self):
        return dict(CITIES).get(self.city_name)
