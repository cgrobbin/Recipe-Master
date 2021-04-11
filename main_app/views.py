from django.shortcuts import render, redirect
import uuid
import boto3
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, RecipeForm, UserUpdateForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile, Recipe, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'recipemaster-capstone-0119'
p_folder = 'profiles/'
r_folder = 'recipes/'

# Update Profile Photo
@login_required
def update_photo(request):
    profile = Profile.objects.get(user=request.user)
    photo_file = request.FILES.get('profile-photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = p_folder + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            profile.url = url
            profile.save()
            messages.success(request, f"Photo successfully uploaded")
        except:
            messages.error(request, f"There was an error during upload")
    return redirect('profile')

# New Recipe
@login_required
def recipe_new(request):
    recipe_form = RecipeForm(request.POST or None)
    photo_file = request.FILES.get('recipe-photo-file', None)
    img_url = ''
    if photo_file:
        s3 = boto3.client('s3')
        key = r_folder + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            img_url = url
        except:
            messages.error(request, f"An error occured with the photo upload. A default has been set")
    else:
        img_url = "https://i.imgur.com/RtCoQclt.jpg"

    if request.POST and recipe_form.is_valid():
        new_recipe = recipe_form.save(commit=False)
        new_recipe.author = request.user
        new_recipe.url = img_url
        new_recipe.save()
        messages.success(request, f"Recipe Created")
        return redirect('index')
    else:
        return render(request, 'home.html', { 'recipe_form': recipe_form })

# Update Recipe Photo
@login_required
def recipe_photo(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    photo_file = request.FILES.get('recipe-detail-photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = r_folder + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            recipe.url = url
            recipe.save()
        except:
            messages.error(request, f"An error occured with the photo upload. Please try again")
    return redirect('detail', recipe_id=recipe_id)

# Home
def home(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about.html')

# Profile/Recipe Detail
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user) 
    recipes = Recipe.objects.filter(users=profile)
    return render(request, 'profile.html', { 'profile': profile, 'recipes': recipes })

# Update Profile
@login_required
def update_profile(request):
    user_form = UserUpdateForm(request.POST or None, instance = request.user)
    if request.POST and user_form.is_valid():
        user_form.save()
        messages.success(request, f"Profile Updated")
        return redirect('profile')
    else:
        messages.error(request, f"Profile Update Error")
        return render(request, 'profile.html')

# Signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user, url='https://i.imgur.com/CMqTyEZs.jpg')
            profile.save()
            login(request, user)
            messages.success(request, f"Successful Signup")
            return redirect('profile')
        else:
            messages.error(request, f"Invalid Signup - Try Again")
    form = SignupForm()
    context = { 'form': form}
    return render(request, 'registration/signup.html', context)

# Recipe Index
def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

# Recipe Detail
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    comments = Comment.objects.filter(recipe_id=recipe_id)
    favorited = False
    if request.user:
        profile = Profile.objects.get(user=request.user)
        if profile in recipe.users.all():
            favorited = True
    context = {
        'recipe': recipe,
        'comments': comments,
        'favorited': favorited
    }
    return render(request, 'recipes/detail.html', context)

# Search Results
def search(request):
    query = request.GET['search']
    recipes = []
    recipe_titles = Recipe.objects.filter(title__icontains = query)
    recipe_tags = Recipe.objects.filter(tags__icontains = query)
    for recipe in recipe_titles:
        recipes.append(recipe)
    for recipe in recipe_tags:
        recipes.append(recipe)
    return render(request, 'recipes/search.html', { 'recipes': recipes, 'query': query })

# Edit Recipe
@login_required
def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    if request.POST and recipe_form.is_valid():
        recipe_form.save()
        messages.success(request, f"Recipe Edited")
        return redirect('detail', recipe_id=recipe_id)
    else:
        messages.error(request, f"An error occuring duriing save")
        return redirect('detail', recipe_id=recipe_id)

# Delete Recipe
@login_required
def recipe_delete(request, recipe_id):
    Recipe.objects.get(id=recipe_id).delete()
    return redirect('index')

# New Comment
@login_required
def comment_new(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = Profile.objects.get(user=request.user)
    comment_form = CommentForm(request.POST or None)
    if request.POST and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.recipe = recipe
        new_comment.user = profile
        new_comment.save()
        messages.success(request, f"Comment Posted")
        return redirect('detail', recipe_id=recipe_id)
    else:
        messages.success(request, f"Error in posting comment")

# Edit Comment
@login_required
def comment_edit(request, comment_id, recipe_id):
    comment = Comment.objects.get(id=comment_id)
    comment_form = CommentForm(request.POST or None, instance=comment)
    if request.POST and comment_form.is_valid():
        comment_form.save()
        messages.success(request, f"Comment edited")
        return redirect('detail', recipe_id=recipe_id)
    else:
        messages.error(request, f"Error is editing comment")

# Delete Comment
@login_required
def comment_delete(request, comment_id, recipe_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('detail', recipe_id=recipe_id)

# Add Recipe to Favorites
@login_required
def add_favorite(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = Profile.objects.get(user=request.user)
    if profile in recipe.users.all():
        messages.error(request, f"Recipe Already Favorited")
    else:
        recipe.users.add(profile)
        messages.success(request, f"Recipe Favorited")
        return redirect('detail', recipe_id=recipe_id)

# Remove Recipe from Favorites
@login_required
def remove_favorite(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    profile = Profile.objects.get(user=request.user)
    if profile in recipe.users.all():
        recipe.users.remove(profile)
        messages.success(request, f"Recipe Remove from Favorites")
        return redirect('detail', recipe_id=recipe_id)
    else:
        messages.error(request, f"You have not favorited this recipe")
