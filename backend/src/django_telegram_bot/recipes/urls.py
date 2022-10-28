
from django.contrib import admin
from django.urls import path, include
from .views import RecipeSingle, ProfileSingle, RecipesList, ProfileList
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('resipies/', RecipesList.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('resipe/<int:pk>/', RecipeSingle.as_view()),
    path('profile/<int:pk>/', ProfileSingle.as_view()),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout' ),

]
