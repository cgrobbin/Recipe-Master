from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/update_photo/', views.update_photo, name='update_photo'),
    path('accounts/profile/update_profile/', views.update_profile, name='update_profile'),
    path('search/', views.search, name='search'),
    path('recipes/', views.recipe_index, name='index'),
    path('recipes/new/', views.recipe_new, name='recipe_new'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('recipes/<int:recipe_id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('recipes/<int:recipe_id>/remove_favorite/', views.remove_favorite, name='remove_favorite'),
    path('recipes/<int:recipe_id>/recipe_photo/', views.recipe_photo, name='recipe_photo'),
    path('recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
    path('recipes/<int:recipe_id>/comment/new/', views.comment_new, name='comment_new'),
    path('recipes/<int:recipe_id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('recipes/<int:recipe_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]