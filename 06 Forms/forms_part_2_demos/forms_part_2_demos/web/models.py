from django.db import models

from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_NAME_LEN = 20
    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3
    MAX_LEN_TEXT = 25
    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    # Relation with another model
    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
