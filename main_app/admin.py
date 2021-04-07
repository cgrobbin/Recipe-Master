from django.contrib import admin
from .models import Profile, Recipe, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Comment)