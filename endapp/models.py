from msilib import Table
from pyexpat import model
from django.db import models

# Create your models here.
class Player(models.Model):
    p_id = models.IntegerField()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = models.CharField(max_length=15)
    overall = models.IntegerField()
