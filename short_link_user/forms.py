from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from short_link_user.models import ShortedLink


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GenerateShortLinkForm(forms.ModelForm):
    link = forms.URLField()

    class Meta:
        model = ShortedLink
        fields = ['link']
