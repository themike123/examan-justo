from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from accounts.models import State, Hitman

class Hit(models.Model):
    hitman = models.ForeignKey(Hitman , on_delete=CASCADE)
    description = models.TextField(blank=True)
    target = models.CharField(max_length=50)
    status = models.ForeignKey(State, on_delete=CASCADE)
    creator = models.ForeignKey(User, on_delete=CASCADE, editable=False)

    def __str__(self):
        return self.target

