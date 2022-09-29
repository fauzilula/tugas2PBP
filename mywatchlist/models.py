from django.db import models

# Create your models here.
class mywatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=225)
    review = models.TextField()