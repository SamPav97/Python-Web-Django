from django import forms
from django.shortcuts import render

from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person


def index_form(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        # if it's post
        form = PersonForm(request.POST)
        # Is valid is a function that is necessary and does a bunch of importnt things.
        # It validates form and fills cleaned data.
        form.is_valid()
        name = form.cleaned_data['your_name']
        # When you have the name create me an object with that name in DB
        Person.objects.create(
            name=name,
        )
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    story = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Person
        fields = '__all__'


def index_model_forms(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save() # Same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html', context)
