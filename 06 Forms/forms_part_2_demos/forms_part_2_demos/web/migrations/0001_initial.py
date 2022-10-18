# Generated by Django 4.1.2 on 2022-10-18 11:30

from django.db import migrations, models
import forms_part_2_demos.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25, validators=[forms_part_2_demos.web.validators.validate_text])),
                ('priority', models.IntegerField(validators=[forms_part_2_demos.web.validators.ValueInRangeValidator(1, 10)])),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
