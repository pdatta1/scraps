from django.forms import forms
from .models import ScrapUser
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = ScrapUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
