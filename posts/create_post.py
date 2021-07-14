from django import forms
from .models import Post
from datetime import datetime
from django.utils.text import slugify
from .models import ScrapUser


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['created_on', 'updated', 'slug', 'author']

    def save(self, commit=True):
        post = super(CreatePostForm, self).save(commit=False)
        post.title = self.cleaned_data['title']
        post.city_name = self.cleaned_data['city_name']
        post.content = self.cleaned_data['content']
        post.slug = slugify(post.title)
        post.status = self.cleaned_data['status']
        post.phone_number = self.cleaned_data['phone_number']
        post.email_address = self.cleaned_data['email_address']
        post.created_on = datetime.now()
        post.updated = datetime.now()

        if commit:
            post.save()
        return post


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['created_on', 'updated', 'slug', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['style'] = 'width:800px; height: 400px;'

    def save(self, commit=True):
        post = super(EditPostForm, self).save(commit=False)
        post.title = self.cleaned_data['title']
        post.city_name = self.cleaned_data['city_name']
        post.content = self.cleaned_data['content']
        post.slug = slugify(post.title)
        post.status = self.cleaned_data['status']
        post.phone_number = self.cleaned_data['phone_number']
        post.email_address = self.cleaned_data['email_address']
        post.created_on = datetime.now()
        post.updated = datetime.now()

        if commit:
            post.save()
        return post
