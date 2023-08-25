from rest_framework import serializers
from blogapps.models import UserPost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'