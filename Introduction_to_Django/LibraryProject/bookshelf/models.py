from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # published_date = models.DateField()

    # isbn = models.CharField(max_length=13, unique=True)
    # pages = models.IntegerField()
    # cover_image = models.URLField(blank=True)
    # language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
