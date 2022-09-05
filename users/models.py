from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    STATUS = (
        ('owner', 'owner'),
        ('observer', 'observer'),
        ('moderator', 'moderator')
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=128, choices=STATUS, default='observer')
    description = models.TextField('Description', max_length=512, default='', blank=True)

    def __str__(self):
        return self.username
