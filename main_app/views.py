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

# Profile/Recipe Detail
# To add to correct folder, add folder name to url, ****TALK TO TA OR INSTRUCTOR ABOUT CONFIGURATION****