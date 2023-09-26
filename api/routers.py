from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import apiviews


router = routers.DefaultRouter()

router.register(r"movies/", apiviews.get_movies, basename="movies")
urlpatterns = router.urls

#suffix
#urlpatterns = format_suffix_patterns(urlpatterns)