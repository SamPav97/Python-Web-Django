from django.contrib.auth import forms as auth_forms, get_user_model


UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    # One way to do placeholders. another is w template tag. See templatetags file and filters in template
    # placeholders = {
    #     'username': 'Username: '
    # }

    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            "username": auth_forms.UsernameField

        }
