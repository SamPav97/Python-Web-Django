from django.urls import path

from todo.api_auth.views import RegisterApiView, LoginApiView

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', LoginApiView.as_view(), name='api login user'),
)
