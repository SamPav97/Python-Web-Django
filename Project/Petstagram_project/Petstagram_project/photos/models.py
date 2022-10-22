# photos/models.py
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from Petstagram_project.core.model_mixins import StrFromFieldsMixin
from Petstagram_project.pets.models import Pet
from Petstagram_project.photos.validators import validate_file_less_than_5mb

'''
The field Photo is required:
•	Photo - the user can upload a picture from storage, the maximum size of the photo can be 5MB
The fields description and tagged pets are optional:
•	Description - a user can write any description of the photo; it should consist of a maximum of 300 characters and a minimum of 10 characters
•	Location - it should consist of a maximum of 30 characters
•	Tagged Pets - the user can tag none, one, or many of all pets. There is no limit on the number of tagged pets
There should be created one more field that will be automatically generated:
•	Date of publication - when a picture is added or edited, the date of publication is automatically generated
'''


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    # Requires media file to work correctly.
    photo = models.ImageField(
        # mediafiles for upload is by default because its in settings
        upload_to='pet_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django/Python validation not internal to DB
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Auto set current date on save
        auto_now=True,
        null=False,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations

    # Many-to-many relations
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

