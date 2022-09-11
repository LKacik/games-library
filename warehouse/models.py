from django.db import models

# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    description = models.TextField()
    platform = models.CharField(max_length=192)
    image = models.ImageField()
    released = models.DateField()


