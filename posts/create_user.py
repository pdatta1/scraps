from django.forms import forms
from .models import ScrapUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class CreateUserForm(UserCreationForm):
    class Meta:
        model = ScrapUser
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
       
        user.save()
        return user
