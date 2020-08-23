from django.db import models

# Create your models here.
  
class Entry(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.headline