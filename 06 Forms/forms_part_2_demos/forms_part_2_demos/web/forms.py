from django import forms
from django.core.exceptions import ValidationError

from forms_part_2_demos.web.model_validators import validate_max_todos_per_person
from forms_part_2_demos.web.models import Todo, Person
from forms_part_2_demos.web.validators import validate_text, validate_priority, ValueInRangeValidator


class ToDoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        )
    )


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()
    # Clean method does two things.
    # 1-It transforms data into desired format.
    # 2-Validation

    def clean_text(self):
        return self.cleaned_data['text'].lower()

    # Here is how clean can be used to transform data
    # into desired format/form/state. What I do is tell it
    # if this person is full of tasks assign it to unassigned.
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']

        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')

        return assignee

    # here clean is used as validation and an error is thrown if false.
    # def clean_assignee(self):
    #     assignee = self.cleaned_data['assignee']
    #     validate_max_todos_per_person(assignee)
    #     return assignee

