from rest_framework import serializers
from .models import Profile, Recipes


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'telegram_username', 'name', 'gender']


class RecipesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'recipe_name', 'description']

