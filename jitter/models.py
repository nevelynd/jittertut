from django.db import models
from django import  forms

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.username  + " " + self.photo   


class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="fromuser")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="touser")
    time = models.DateTimeField('time')
    def __str__(self):
        return self.from_user.username + " bunked " + self.to_user.username # Create your models here.



class Bunkform(models.Model):
    your_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)

