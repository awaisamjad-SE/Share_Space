from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title', 'text', 'description', 'photo', 'is_private']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a catchy title for your post...'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'What\'s the main content of your post?'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Add more details about your post (optional)...'
            }),
        }
        

class UserRegistrationForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    class Meta:
        model= User
        fields = ('username', 'email', 'password')