from django.db import models
from django.core import validators

from .validators import validate_that_it_starts_with_letter, validate_if_name_contains_only_letters


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=25,
                                  validators=[validators.MinLengthValidator(2), validate_that_it_starts_with_letter,])
    last_name = models.CharField(max_length=35,
                                 validators=[validators.MinLengthValidator(1), validate_that_it_starts_with_letter,])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[validators.MinLengthValidator(8)])
    image = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, default=18)


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=(validators.MinLengthValidator(2), validate_if_name_contains_only_letters))
    image = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True, null=True)

