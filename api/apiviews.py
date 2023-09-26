from api.models import Movies
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import MovieSerializer


@api_view(["GET", "POST"])
def get_movies(request, format=None):
    """
    get all the movie details like title, director, year, writer, desription.
    """
    if request.method == "GET":
        movies = Movies.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        return Response(data=movie_serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == "POST":
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            return Response(data=movie_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(movie_serializer.errors, status=status.HTTP_404_NOT_FOUND)
    