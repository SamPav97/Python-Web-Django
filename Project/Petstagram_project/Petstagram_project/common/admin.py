from django.contrib import admin

from Petstagram_project.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
