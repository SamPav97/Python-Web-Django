from django.shortcuts import render, redirect, resolve_url
import pyperclip
from django.urls import reverse

from Petstagram_project.common.forms import PhotoCommentForm, SearchPhotosForm
from Petstagram_project.common.models import PhotoLike
from Petstagram_project.common.utils import get_user_liked_photos, get_photo_url
from Petstagram_project.core.photo_utils import apply_likes_count, apply_user_liked_photo
from Petstagram_project.photos.models import Photo


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': SearchPhotosForm(),
    }
    return render(request, 'common/home-page.html', context,)


def like_photo(request, photo_id):
    # TODO: Fix when auth so like and unlike happens.
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:

        # Option 2:

        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    return redirect(get_photo_url(request, photo_id))

    # Option 1 for creating object:
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False) # commit false does not send to db but returns the obj which we will send to db
        comment.photo = photo
        comment.save()

    return redirect('index')
