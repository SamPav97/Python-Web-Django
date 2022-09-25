from random import choice

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }

    return render(request, 'departments/all.html', context)


def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    return redirect(f'/departments/?order_by= {order_by}')
