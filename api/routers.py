from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from . import apiviews


schema_view = get_schema_view(
   openapi.Info(
      title="Movie API REST",
      default_version='v1',
      description="This API REST allow the user to get, add, delete and update his movies, also allow the user to register, login and logout.",
      terms_of_service="https://github.com/AndresSilverall",
      contact=openapi.Contact(email="andresfsilverall0109@gmail.com"),
      license=openapi.License(name="MIT license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path('api/register/', apiviews.register_user, name='register'),
    path('api/login/', apiviews.login_user, name='login'),
    path('api/logout/', apiviews.logout_user, name='logout'),
    path('api/movies/', apiviews.get_all_movies, name='get_all_movies'),
    path('api/movie/detail/<int:pk>', apiviews.get_movie_detail, name='get_movie_detail'),
    path('api/add/movie/', apiviews.add_movie, name='add_movie'),
    path('api/update/movie/<int:pk>', apiviews.update_movie, name='update_movie'),
    path('api/delete/movie/<int:pk>', apiviews.delete_movie, name='delete_movie'),
    path('api/favorite/movie/', apiviews.favorite_movie, name='favorite_movie'),
    path('api/review/movie/', apiviews.review_movie, name='review_movie'),

    #Documentation with Swagger: endpoints
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='apidoc'),
]


#suffix
#urlpatterns = format_suffix_patterns(urlpatterns)