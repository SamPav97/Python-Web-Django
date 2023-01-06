
from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions
from rest_framework import generics as rest_generic_views, views as rest_views
from rest_framework import serializers
from rest_framework.authtoken import views as authtoken_views
from rest_framework.authtoken import models as authtoken_models
from rest_framework.response import Response

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    # Make user with hashed pass.
    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    # Necessary to make sure password is validated by Django validators.
    def validate(self, data):
        # Invoke password validators
        user = UserModel(**data)
        password = data.get('password')
        errors = {}
        try:
            password_validation.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)

    # Tells serializer what we want returned.
    def to_representation(self, instance):
        # Below is a dictionary that returns in browser
        # I simply pop the pass, so it don't return
        user_representation = super().to_representation(instance)
        user_representation.pop('password')
        return user_representation


class RegisterApiView(rest_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginApiView(authtoken_views.ObtainAuthToken):
    # Copy, paste from documentation on how to log in view.
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = authtoken_models.Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })


class LogoutApiView(rest_views.APIView):
    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)

    @staticmethod
    def __perform_logout(self, request):
        request.user.authtoken.delete()
        return Response({
            'message': 'user logged out'
        })
