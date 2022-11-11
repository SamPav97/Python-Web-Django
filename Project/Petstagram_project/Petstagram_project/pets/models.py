# pets/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from Petstagram_project.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()
'''
The fields Name and Pet Photo are required:
•	Name - it should consist of a maximum of 30 characters.
•	Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
•	Date of Birth - pet's day, month, and year of birth
'''


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30
    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    # When no slug is given, slug is generated.
    def save(self, *args, **kwargs):
        # Create/update so that the thing is in db, so it has self.id
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)