from django.contrib import admin
from api.models import Movie, FavoriteMovie, ReviewMovie


# Register your models here.s
admin.site.register(Movie)
admin.site.register(FavoriteMovie)
admin.site.register(ReviewMovie)
