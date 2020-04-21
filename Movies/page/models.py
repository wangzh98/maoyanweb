from django.db import models


class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    ranking = models.CharField(max_length=20)
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'movies'
