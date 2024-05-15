from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False, unique=True,)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)



    def __str__(self):
        return self.username +  ' | ' + self.email





class PlaceHolder(models.Model):
    ...

    def __str__(self):
        ...