from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class CustomUser(AbstractUser):
    pass
    # username = models.CharField(max_length=120, unique=True)
    # email = models.EmailField(unique=True, null=True)
    #
    # def __str__(self):
    #     return self.username