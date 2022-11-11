from django import forms

from Petstagram_project.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__' # We need to skip slug so:
        # fields = ('name', 'personal_photo', 'date_of_birth') # same as:
        exclude = ('slug', 'user')
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


class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['readonly'] = 'readonly'


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    # Another way to set widgets to readonly and disabled. The other is through labels in the meta class.
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    # We override the save method to actually delete. con otherwise how do we delete?
    # This is only done for the delete class.
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance


