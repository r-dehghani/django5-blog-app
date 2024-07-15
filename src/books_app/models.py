from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return (self.title)