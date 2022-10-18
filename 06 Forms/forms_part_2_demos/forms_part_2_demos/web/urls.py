from django.urls import path

from forms_part_2_demos.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
