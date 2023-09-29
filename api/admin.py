from django.contrib import admin
from api.models import Movies, FavoriteMovie, ReviewMovie


# Register your models here.s
admin.site.register(Movies)
admin.site.register(FavoriteMovie)
admin.site.register(ReviewMovie)
