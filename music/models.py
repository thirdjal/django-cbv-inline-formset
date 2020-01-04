from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} - {self.name}"
