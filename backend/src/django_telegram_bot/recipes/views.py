from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import Recipes, Profile
from .serializers import ProfileSerializers, RecipesSerializers


class RecipesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RecipeSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers


class ProfileSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers




