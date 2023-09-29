from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(
        max_length=60, 
        null=False, 
        blank=False, 
        unique=True)
    
    description = models.TextField(null=False)
    genre = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="movies/", null=True)
    director = models.CharField(max_length=30, null=False)
    writer = models.CharField(max_length=30, null=False)
    year = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.title
    

class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie)


class ReviewMovie(models.Model):

    class ScoreMovie(models.TextChoices):

        ONE = "1", "one",
        TWO = "2", "two"
        THREE = "3" "three"
        FOUR = "4", "four"
        FIVE = "5", "five"
        SIX = "6", "six"
        SEVEN = "7", "seven"
        EIGHT = "8", "eight"
        NINE = "9", "nine"
        TEN = "10", "ten"
    
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    score = models.CharField(choices=ScoreMovie.choices, null=True, max_length=6)
    review = models.TextField(verbose_name="review movie", null=True)


    def __str__(self):
        return self.score
