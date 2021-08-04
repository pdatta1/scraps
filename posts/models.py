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

Flags = (
    (0, 'saved'),
    (0, 'report'),
)

GENDER = (
    (0, 'male'),
    (1, 'female'),
    (2, 'other'),
)
def user_profilepic_path(instance, filename):
    return '{0}/{0}'.format(instance.user.id,images_path(filename))


class ScrapUser(AbstractUser):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'ScrapUser'
        unique_together = ('email',)

class Profile(models.Model):
    user = models.OneToOneField(ScrapUser, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to=user_profilepic_path, null=True, blank=True, default='')
    status = models.IntegerField(choices=GENDER, default=0)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.user)

    
    def get_gender_name(self):
        return dict(GENDER).get(self.gender)    

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
    title = models.CharField(max_length=30, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(scrapsettings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post')
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    brief = models.TextField(max_length=100, default='')
    created_on = models.DateTimeField(auto_now=True)
    pumps = models.ManyToManyField(ScrapUser, related_name='blog_post_pumps')
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


    def number_of_pumps(self):
        self.pumps.count()



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    context = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:

        ordering = ['date_created']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return 'Comment: {0} - {0}'.format(self.post.title, self.profile)



class SubComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='sub_comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    context = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:

        ordering = ['date_created']
        verbose_name = 'sub_comment'
        verbose_name_plural = 'sub_comments'
    
    def __str__(self):
        return 'Sub_Comment: {0} - {0}'.format(self.comment.post.title, self.profile)
