from django import forms

from Petstagram_project.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__' # We need to skip slug so:
        # fields = ('name', 'personal_photo', 'date_of_birth') # same as:
        exclude = ('slug',)
        # To set the labels as you wish them (text before input box)
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        # To have placeholders for text fields:
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    pass

