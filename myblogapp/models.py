from django.db import models

# Create your models here.
class course(models.Model):
   deparment = models.IntegerField(max_length=100)
   coursenAme = models.CharField(max_length=50)
   coursecode =  models.CharField(max_length=50)
