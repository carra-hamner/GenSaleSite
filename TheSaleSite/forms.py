from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import ListItem


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ListingForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ('name', 'contact_email', 'list_option', 'price', 'description')


