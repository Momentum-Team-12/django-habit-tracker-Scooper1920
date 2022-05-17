from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Habit (models.Model):
    iWantTo = models.CharField(max_length=100, null=True)
    goal    = models.IntegerField(blank =True, null=True)
    user    = models.ForeignKey( )
