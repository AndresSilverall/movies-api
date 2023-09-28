from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(
        max_length=25, 
        null=False, 
        blank=False, 
        unique=True)
    
    description = models.TextField(null=False)
    genre = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to="media/movies", null=True)
    director = models.CharField(max_length=30, null=False)
    writer = models.CharField(max_length=30, null=False)
    year = models.PositiveIntegerField(null=False)


    def __str__(self):
        return self.title
    

class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie


class ReviewMovie(models.Model):
    SCORE_MOVIE = (
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
        ("ten", "10")
    )

    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    score = models.CharField(choices=SCORE_MOVIE, null=True, max_length=6)


    def __str__(self):
        return self.score
