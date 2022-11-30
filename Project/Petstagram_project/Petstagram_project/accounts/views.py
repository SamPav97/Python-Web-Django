from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import render

# Always get the user model with this function and then use it:
# Else only have the actual name of the user model in the class that is itself and in the settings where you nominate\
# it as new user.
from Petstagram_project.accounts.forms import UserCreateForm
from Petstagram_project.photos.models import Photo

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    # Form class replaces the necessity for model. It is overwritten in the form.
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()

        photos = self.object.photo_set \
            .order_by('-publication_date')

        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the user is the owner of this profile show edit page (see temp for show edit page). I need it in ctxt
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()
        # get objects that have foreign key to current object:

        photos = self.object.photo_set \
            .prefetch_related('photolike_set') #if we use .all it will break the n+1query set

        context['photos_count'] = photos.count()
        # We need likes now, but we need all likes for all photos that belong to us. The sum below makes sense. think!
        # This is called n+1 query problem. for object n we make n+1 calls to db
        # it means that when we need info for diff object we dont make as many calls as objects but we make one call
        #that includes all objects.
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        context['photos'] = self.get_paginated_photos()
        context['pets'] = self.object.pet_set.all()
        return context


class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')



