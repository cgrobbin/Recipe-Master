from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
#     path('signup/', views.signup, name='signup'),
#     path('accounts/profile', views.profile, name='profile'),
#     path('recipes/', views.recipe_index, name='index'),
#     path('recipes/search/', views.search, name='search'),
#     path('recipes/<int:rec_id>/', views.recipe_detail, name='detail'),

# Admin purposes
    # path('recipes/<int:rec_id>/edit', views.recipe_edit, name='recipe_edit'),
    # path('recipes/<int:rec_id>/delete', views.recipe_delete, name='recipe_delete'),

#     path('recipes/new/', views.recipe_new, name='recipe_new'),
#     path('recipes/<int:rec_id>/comment/new', views.comment_new, name='comment_new'),
#     path('recipes/<int:rec_id>/comment/<int:com_id>/edit/', views.comment_edit, name='comment_edit'),
#     path('recipes/<int:rec_id>/comment/<int:com_id>/delete', views.comment_delete, name='comment_delete'),
]