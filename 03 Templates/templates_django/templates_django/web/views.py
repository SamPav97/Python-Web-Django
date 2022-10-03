import random
from datetime import datetime

from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}'


def index(request):
    context = {
        'title': 'softUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Doncho', 19),
        'now': datetime.now(),
        'students': [
            'Pesho',
            'Gosho',
            'Maria',
            'Stamat',
        ],
        'values': list(range(20)),
    }
    return render(request, 'index.html', context)