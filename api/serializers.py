from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from api.models import Movies, FavoriteMovie, ReviewMovie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_url_img')
    class Meta:
        model = Movies
        fields = (
            "id", 
            "title", 
            "description", 
            "director",
            "genre",
            "image",
            "writer", 
            "year"
        )
        read_only_fields = ('image',)

    def get_url_img(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.image.url)
        return None  



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


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ("id", "movie")