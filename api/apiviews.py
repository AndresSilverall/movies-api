from api.models import Movies
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import MovieSerializer, UserRegistrationSerializer


@api_view(["GET"])
def get_all_movies(request, format=None):
    """
    The user make a request to get all the resources stored on the DB.

    Example: 'api/movies/'

    Returns: All the movies. 

    """
    if request.method == "GET":
        movie = Movies.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        return Response(data=movie_serializer.data, status=status.HTTP_200_OK)
    

@api_view(["GET"])
def get_movie_detail(request, pk: int):
    """
    Args: The primary key of the model 'Movies'.
    
    Example: 'api/movie-detail/2'

    Returns: The movie details like title, description, director,
    writer, year.

    """
    if request.method == "GET":
        movie = Movies.objects.filter(id=pk).first()
        if movie is not None:
            movie_serializer = MovieSerializer(movie, many=False)

            return Response(data=movie_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Movie not found!",
                "status": status.HTTP_404_NOT_FOUND
            })



@api_view(["POST"])
def add_movie(request):
    """
    The user can store a new movie on the DB.

    Example: 'api/add-movie/'

    Returns: A message with the new movie added.

    """
    if request.method == "POST":
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response({
                "message": "Movie added successfully!",
                "status": status.HTTP_201_CREATED
            })
        else:
            return Response(data=movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["PUT"])
def update_movie(request, pk: int):
    """
    Update movie.

    Args: The primary key of the model 'Movies'.

    Example: 'api/update-movie/id'

    Returns: A message with the movie updated.

    """
    if request.method == "PUT":
        movie = Movies.objects.filter(id=pk).first()
        if movie is not None:
            movie_serializer = MovieSerializer(movie, data=request.data)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return Response({
                    "message": "Movie updated successfully!",
                    "status": status.HTTP_201_CREATED
                })
            else:
                return Response(data=movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def delete_movie(request, pk: int):
    """
    Args: The primary key of the model 'Movies'.

    Example: 'api/delete-movie/4'

    Returns: A message with the movie deleted.

    """
    try:
        movie = Movies.objects.filter(id=pk)
                
        if request.method == "DELETE":
            movie.delete()
            return Response({
                "message": "Movie deleted!",
                "status": status.HTTP_200_OK
            })
        
    except Movies.DoesNotExist as e:
        return Response({
            "message": "Error, movie not found!",
            "status": str(e)
        })


#-----This section is about the Authentication------
@api_view(["POST"])
@permission_classes(AllowAny)
def register_user(request):
    user_serializer = UserRegistrationSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response({
            "message": "User registered successfully!",
            "status": status.HTTP_200_OK
        })
    return Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)