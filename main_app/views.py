from django.shortcuts import render, redirect
import uuid
import boto3
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth import login

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'recipemaster-capstone-0119'

# Home
def home(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about.html')

# # Profile/Recipe Detail
# # To add to correct folder, add folder name to url s3/bucket/folder/key
def profile(request):
    return render(request, 'profile.html')

# Signup
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid Signup - Try Again'
    form = SignupForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)

# # Recipe Index
# def recipe_index(request):
#     return

# # Search Results
# def search(request):
#     return

# # Recipe Detail
# def recipe_detail(request):
#     return

# # New Recipe
# def recipe_new(request):
#     return

# # New Comment
# def comment_new(request):
#     return

# # Edit Comment
# def comment_edit(request):
#     return

# # Delete Comment
# def comment_delete(request):
#     return

# # Edit Recipe
# def recipe_edit(request):
#     return

# # Delete Recipe
# def recipe_delete(request):
#     return