from django.db import models
from django.contrib.auth.models import AbstractUser
import scrap_post.settings as scrapsettings
from django.template.defaultfilters import slugify
from django.urls import reverse
from uuid import uuid4
import os

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
        unique_together = ('email',)
def images_path(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]

        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper 


def user_directory_path(instance, filename):
    return '{0}/{0}'.format(instance.id, images_path(filename))



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
    image1 = models.ImageField(upload_to='upload/{}'.format(user_directory_path), null=True, blank=True, default='')
    image2 = models.ImageField(upload_to='upload/{}'.format(user_directory_path), null=True, blank=True, default='')
    image3 = models.ImageField(upload_to='upload/{}'.format(user_directory_path), null=True, blank=True, default='')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('posts:index')

    def get_city_name(self):
        return dict(CITIES).get(self.city_name)

