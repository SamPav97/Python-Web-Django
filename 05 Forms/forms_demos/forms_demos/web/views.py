
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


class Person


def index_model_forms(request):
    context = {
    }
    return render(request, 'model_forms.html', context)
