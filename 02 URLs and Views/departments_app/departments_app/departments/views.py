from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def sample_view(request: HttpRequest, *args, **kwargs):
    order_by = request.GET.get('order_by', 'name')
    body = f'path: {request.path}, args={args}, kwargs={kwargs}, order_by: {order_by}'


    return HttpResponse(body)


def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)
