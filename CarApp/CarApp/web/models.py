from django.db import models
from django.core import validators
from django.db import models
from CarApp.web.validators import validate_min_chars, validate_year_included


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 18
    NAMESPASS_MAX_LENGTH = 30
    user = models.B

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            validate_min_chars,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        # TODO check if this works
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
        ),
        null=False,
        blank=False,
    )

    # TODO in forms make it into pass field with widgets.
    password = models.CharField(
        max_length=NAMESPASS_MAX_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=NAMESPASS_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=NAMESPASS_MAX_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    GENRE_MAX_LENGTH = 30
    MINIMAL_PRICE = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER_CAR = "Other"

    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER_CAR, OTHER_CAR),
    )
    # TODO why do we have max length if its selection?
    type = models.CharField(
        choices=CARS,
        max_length=TYPE_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(MODEL_MIN_LENGTH),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
          validate_year_included,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MINIMAL_PRICE),
        ),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)
