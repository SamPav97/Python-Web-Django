from django.shortcuts import render, redirect

from CarApp.web.forms import ProfileAddForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from CarApp.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home.html', context)


def catalogue(request):
    profile = get_profile()
    context = {
        'cars': Car.objects.all(),
        'cars_count': Car.objects.all().count(),
        'profile': profile,
    }
    return render(request, 'catalogue.html', context)


def add_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileAddForm()
    else:
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-create.html', context,)


def details_profile(request):
    profile = get_profile()
    all_cars = Car.objects.all()
    total_price = 0
    for car in all_cars:
        total_price += float(car.price)
    context = {
        'profile': profile,
        'total_price':total_price
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-edit.html', context)


def add_car(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'cars/car-create.html', context,)


def details_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()
    context = {
        'car': car,
        'profile': profile,
    }
    return render(request, 'cars/car-details.html', context,)


def edit_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    profile = get_profile()
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }
    return render(request, 'cars/car-delete.html', context)
