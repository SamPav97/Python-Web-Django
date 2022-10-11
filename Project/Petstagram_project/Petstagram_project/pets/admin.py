from django.contrib import admin

# Register your models here.
from Petstagram_project.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
