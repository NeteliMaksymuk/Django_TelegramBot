from django.db import models


class Profile(models.Model):
    GENDER = [
        ('m', 'male'),
        ('f', 'female'),
        ('c', 'co-ed'),
    ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        verbose_name='first_name',
        max_length=48,
        null=True
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=48,
        null=True
    )
    telegram_username = models.CharField(
        verbose_name='telegram_username',
        max_length=48
    )
    name = models.CharField(
        verbose_name='name',
        max_length=48
    )
    gender = models.CharField(
        max_length=6,
        verbose_name='gender',
        choices=GENDER
    )

    class Meta:
        verbose_name = 'Profile'




class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(
        verbose_name='recipe_name',
        max_length=48
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Recipes'

