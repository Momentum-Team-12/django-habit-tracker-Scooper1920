from unicodedata import name
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class CustomUser(AbstractUser):
   
    def __str__(self):
        return self.username

class Habit(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)
    goal        = models.IntegerField(null=True, blank =True)
    user        = models.ForeignKey('CustomUser', related_name='habits', on_delete=models.CASCADE, null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    unit        = models.CharField(max_length=100, null=True, blank=True)
    planstart   = models.DateField(null=True, blank=True)
    journal     = models.TextField(null=True, blank=True)
    
    class Meta:
            constraints  = [
                models.UniqueConstraint(fields =['name','planstart'], name='unique_habit')
            ]

    def __str__(self):
        return self.name
    
    
    
    
class DateRecord(models.Model):    
    habit       =   models.ForeignKey('Habit', related_name='date_records', on_delete=models.CASCADE, null= True, blank=True)
    actual      =   models.IntegerField(null=True, blank=True)
    date        =   models.DateField(null=True, blank=True)
    created_at  =   models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
            constraints  = [
                models.UniqueConstraint(fields =['habit','date'], name='unique_date')
            ]

    
    def __str__(self):
        return str(self.date)
