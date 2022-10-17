from django.urls import path

from forms_demos.web.views import index_form, index_model_forms

urlpatterns = (
    path('', index_form, name='index'),
    path('modelforms/', index_model_forms, name='model forms')
)

