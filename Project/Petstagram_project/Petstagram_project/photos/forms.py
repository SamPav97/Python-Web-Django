from django import forms
from django.core.exceptions import ValidationError

from Petstagram_project.common.models import PhotoLike, PhotoComment
from Petstagram_project.pets.forms import DisabledFormMixin
from Petstagram_project.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo',)


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            # delete all connections many to many
            self.instance.tagged_pets.clear()
            # delete a one to many connection:
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            # to then be allowed to delete the current instance
            self.instance.delete()

        return self.instance

