from django.db import models

# Create your models here.
class course(models.Model):
   firstname = models.IntegerField(max_length=100)
   email = models.CharField(max_length=50)
   address =  models.CharField(max_length=50)



class studentdata (models.Model):
   department = models.CharField(max_length=50)
   coursename = models.CharField(max_length=50)
   coursecode = models.CharField(max_length=50)

