from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    url = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user}"
    