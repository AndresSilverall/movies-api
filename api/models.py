from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=25, null=False, blank=False)
    description = models.TextField(null=False)
    director = models.CharField(max_length=30, null=False)
    writer = models.CharField(max_length=30, null=False)
    year = models.PositiveIntegerField(null=False)


    def __str__(self):
        return self.title

