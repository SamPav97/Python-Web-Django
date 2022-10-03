from django.urls import path

from templates_django.web.views import index, redirect_to_home, about

urlpatterns = (
    path('', index, name='index'),
    path('go-to-home/', redirect_to_home, name='redirect to home'),
    path('about/', about, name='about'),
)