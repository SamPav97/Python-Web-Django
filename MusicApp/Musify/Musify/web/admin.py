from django.contrib import admin

from Musify.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class ProfileAdmin(admin.ModelAdmin):
    pass
