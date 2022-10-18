
from django.http import HttpResponse
from django.shortcuts import render

from forms_part_2_demos.web.forms import TodoCreateForm, ToDoForm


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
