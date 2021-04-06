from django.shortcuts import render, redirect
import uuid
import boto3
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, RecipeForm
from django.contrib.auth import login
from .models import Profile, Recipe

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
def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

# # Search Results
# def search(request):
#     return

# # Recipe Detail
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe })

# # New Recipe
def recipe_new(request):
    recipe_form = RecipeForm(request.POST or None)
    if request.POST and recipe_form.is_valid():
        new_recipe = recipe_form.save(commit=False)
        new_recipe.author = request.user
        new_recipe.save()
        return redirect('index')
    else:
        return render(request, 'home.html', { 'recipe_form': recipe_form })

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