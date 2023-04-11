from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=32)
    followers = models.ManyToManyField(to=User, related_name='followers')
    followings = models.ManyToManyField(to=User, related_name='followings')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.username