from django.urls import path

from departments_app.departments.views import sample_view, show_department_details

urlpatterns = (
    path('', sample_view),
    path('<department_id>/', show_department_details),
    path('int/<int:department_id>/', sample_view),
)