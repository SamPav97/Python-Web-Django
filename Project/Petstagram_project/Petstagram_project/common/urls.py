from django.urls import path

from Petstagram_project.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
