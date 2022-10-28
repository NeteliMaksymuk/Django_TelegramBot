
from django.contrib import admin
from django.urls import path, include
from .views import RecipeSingle, ProfileSingle, RecipesList, ProfileList


urlpatterns = [
    path('resipies/', RecipesList.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('resipe/<int:pk>/', RecipeSingle.as_view()),
    path('profile/<int:pk>/', ProfileSingle.as_view()),
    # path('login/', ),
    # path('logout/', ),

]
