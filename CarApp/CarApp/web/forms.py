from django import forms

from CarApp.web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAddForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields disabled
        self.__set_disabled_fields()

    # Overwrite delete method
    def save(self, commit=True):
        # Also delete all albums made by profile
        if commit:
            Car.objects \
                .all() \
                .delete()
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields disabled
        self.__set_disabled_fields()

    # Overwrite delete method
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
