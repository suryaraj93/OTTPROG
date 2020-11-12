from django.db import models


class Language(models.Model):
    lang = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.lang


class Movie(models.Model):
    movie_name = models.CharField(max_length=120, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre = models.CharField(max_length=120)
    starring = models.CharField(max_length=120)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.movie_name



