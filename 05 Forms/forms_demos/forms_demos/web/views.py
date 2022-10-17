from django import forms
from django.shortcuts import render


class NameForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
    )


def index(request):
    context = {
        'form': NameForm()
    }

    return render(request, 'index.html', context)
