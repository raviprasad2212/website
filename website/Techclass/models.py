from pyexpat import model
from time import sleep
from django.db import models

# Create your models here.
class Allcourses(models.Model):
    cousrename = models.CharField(max_length=20)
    insname = models.CharField(max_length=100)

    def __str__(self):
        return self.cousrename

class Details(models.Model):
    course=models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    sp = models.CharField(max_length=200)
    il = models.CharField(max_length=200)

    def __str__(self):
        return self.sp

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
  
    def __str__(self):
        return self.title