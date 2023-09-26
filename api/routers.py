from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import apiviews


urlpatterns = [
    path('api/movies/', apiviews.get_movies, name='movies-list'),
]


#suffix
urlpatterns = format_suffix_patterns(urlpatterns)