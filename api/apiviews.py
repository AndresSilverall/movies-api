from api.models import Movies
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import MovieSerializer


@api_view(["GET"])
def get_movies(request):
    """
    get all the movies
    """
    if request.method == "GET":
        movies = Movies.objects.all()
        movie_serializer = MovieSerializer(movies)
        return Response(data=movie_serializer.data, status=status.HTTP_200_OK)
    