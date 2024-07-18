from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True,)
    def __str__(self) -> str:
        return self.email

