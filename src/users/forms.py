from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class UserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['tz', 'image']
