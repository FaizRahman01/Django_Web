from django.forms import ModelForm
from .models import UserPost

class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = '__all__'