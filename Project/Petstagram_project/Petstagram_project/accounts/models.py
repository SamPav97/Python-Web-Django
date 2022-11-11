from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from Petstagram_project.core.validators import validate_only_letters


class ChoicesEnumMixin:

    # A mixin to test in class and then export
    @classmethod
    def choices(cls):
        # the class method has an iter, so I can iterate thru it.
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


# An enumeration that lets us select between options
class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


# Naming the user model.
class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,

    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),

    )

