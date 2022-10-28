from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Recipes, Profile
from .serializers import ProfileSerializers, RecipesSerializers


class RecipesList(generics.ListCreateAPIView):
        queryset = Recipes.objects.all()
        serializer_class = RecipesSerializers

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RecipeSingle(generics.RetrieveUpdateDestroyAPIView):

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers


class ProfileSingle(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers




