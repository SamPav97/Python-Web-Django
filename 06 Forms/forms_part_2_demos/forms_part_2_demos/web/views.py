
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_part_2_demos.web.forms import TodoCreateForm, ToDoForm, PersonCreateForm
from forms_part_2_demos.web.models import Person


def index(request):
    form_class = ToDoForm
    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        # add request files for media files. and add enctype in form temp.
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list persons')
    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
