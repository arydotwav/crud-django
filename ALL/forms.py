from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'flex items-center justify-center w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Password'
    }))

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Confirm password'
    }))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "content", "completed"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'p-2 rounded-lg', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': "p-2 rounded-lg ", 'placeholder': 'Enter content'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        }
