# Generated by Django 4.1.2 on 2022-10-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pet_person_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
    ]