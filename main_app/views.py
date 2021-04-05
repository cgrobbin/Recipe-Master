from django.shortcuts import render
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'recipemaster-capstone-0119'

# Home
def home(request):
    return render(request, 'home.html')

# About
def about(request):
    return render(request, 'about.html')

# # Profile/Recipe Detail
# # To add to correct folder, add folder name to url, ****TALK TO TA OR INSTRUCTOR ABOUT CONFIGURATION****
# def profile(request):
#     return

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