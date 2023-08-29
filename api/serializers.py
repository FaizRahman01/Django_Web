from rest_framework import serializers
from blogapps.models import UserPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        #set field to '__all__' will return all user fields(username, email, etc)

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = UserPost
        fields = '__all__'

class ManagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'