from Petstagram_project.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    return Pet.objects.filter(slug=pet_slug, user__username=username).get()


# Protects my view from being entered from url directly


def is_owner(request, obj):
    return request.user == obj.user


# Same as above but decorator
class OwnerRequired:
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, *kwargs)

        if request.user == self.object.user:
            return result
        else:
            return '...'
    #def post .... we can reuse them only by inheriting this mixin