from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Boss(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Hitman(models.Model):
    description = models.TextField(blank=True)
    status = models.ForeignKey(State, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.user.username