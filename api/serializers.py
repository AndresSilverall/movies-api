from django.contrib.auth.models import User
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