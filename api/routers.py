from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import apiviews


urlpatterns = [
    path('api/register/', apiviews.register_user, name='register'),
    path('api/movies/', apiviews.get_all_movies, name='get_all_movies'),
    path('api/movie-detail/<int:pk>', apiviews.get_movie_detail, name='get_movie_detail'),
    path('api/add-movie/', apiviews.add_movie, name='add_movie'),
    path('api/update-movie/<int:pk>', apiviews.update_movie, name='update_movie'),
    path('api/delete-movie/<int:pk>', apiviews.delete_movie, name='delete_movie'),

    #Documentation with Swagger: endpoints
    #path('docs/', schema_view, name='docs'),
]


#suffix
#urlpatterns = format_suffix_patterns(urlpatterns)