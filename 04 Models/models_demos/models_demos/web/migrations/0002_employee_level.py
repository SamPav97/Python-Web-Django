# Generated by Django 4.1.2 on 2022-10-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(default='asd', max_length=15),
            preserve_default=False,
        ),
    ]
