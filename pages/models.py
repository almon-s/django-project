from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_title = models.CharField(max_length=50)
    movie_genres = models.CharField(max_length=50)
    char_cast = models.CharField(max_length=50)
    overview = models.CharField(max_length=50)
    release = models.IntegerField
    tag_line = models.CharField(max_length=50)
    avg_rating = models.IntegerField
    vote_count = models.IntegerField