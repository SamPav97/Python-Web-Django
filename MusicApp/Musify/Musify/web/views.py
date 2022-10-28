from django.shortcuts import render, redirect

from Musify.web.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from Musify.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        # TODO add the view for this
        return render(request, 'common/home-no-profile.html')
    context = {
        'albums': Album.objects.all()
    }

    return render(request, 'common/home-with-profile.html', context)


def details_profile(request, pk):

    return render(request, 'profile/profile-details.html',)


def delete_profile(request, pk):
    return render(request, 'profile/profile-delete.html',)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context,)


def edit_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context,)


def delete_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/delete-album.html', context,)
