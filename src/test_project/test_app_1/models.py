from django.db import models

# Create your models here.
class MyModelOne(models.Model):
    name = models.CharField(max_length=16)


class MyModelTwo(models.Model):
    name = models.CharField(max_length=16)


class MyModelThree(models.Model):
    name = models.CharField(max_length=16)
