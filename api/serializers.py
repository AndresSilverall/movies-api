from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from api.models import Movies
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = (
            "id", 
            "title", 
            "description", 
            "director", 
            "writer", 
            "year"
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]


    def create(self, validated_data):
        user = User.objects.create(
        email=validated_data['email'],
        username=validated_data['username'],
        password = make_password(validated_data['password'])

        )
        return user

{
    "username": "pipepk12",
    "email": "pipepk12@gmail.com",
    "password": 3017454086

}