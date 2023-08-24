from django.forms import ModelForm
from .models import UserPost
from django import forms

class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        