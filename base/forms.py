from enum import auto
from django import forms
from .models import Task
from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=20, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
#     class Meta:
#         model = User
#         fields = ('username', 'password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Title', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=250, label='Description', widget=forms.Textarea(attrs={'class':'form-control'}))
    completed = forms.BooleanField(required=False)
    created = forms.HiddenInput()
    
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
    
    
