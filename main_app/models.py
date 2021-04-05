from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    url = models.CharField(
        max_length=250,
        default="https://i.imgur.com/CMqTyEZs.jpg"
        )

    def __str__(self):
        return f"{self.user}"


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    prep_time = models.CharField(max_length=25)
    cook_time = models.CharField(max_length=25)
    servings = models.IntegerField()
    ingredients = ArrayField(models.CharField(max_length=50))
    instructions = ArrayField(models.TextField(max_length=250))
    url = models.CharField(
        max_length=250,
        default="https://i.imgur.com/RtCoQcll.jpg",
        )
    tags = ArrayField(models.CharField(max_length=50))

    def __str__(self):
        return f"{self.title}"
    

