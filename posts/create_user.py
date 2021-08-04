from django import forms
from .models import ScrapUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Password', widget=forms.HiddenInput(), help_text='Minimum 8 characters.', required=False)

    class Meta:
        model = ScrapUser
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'password': None
        }
        fields = ('email',)
        exclude = ['password', 'last-login', 'is_superuser', 'username', 'is_staff', 'is_active', 'date_joined',
                   'post_id',]



class EstablishProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = '__all__'
        exclude = ['user', 'post',]

    def save(self, request, commit=True):
        profile = super(EstablishProfileForm, self).save(commit=False)

        profile.user = request.user
        profile.bio = self.cleaned_data['bio']
        profile.profile_pic = self.cleaned_data['profile_pic']
        profile.status = self.cleaned_data['status']


        
        if commit:
            profile.save()
        return profile 