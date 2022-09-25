from django.urls import path

from departments_app.departments.views import show_departments, show_department_details, redirect_to_first_department

urlpatterns = (
    path('', show_departments),
    path('redirect/', redirect_to_first_department),
    path('<department_id>/', show_departments),
    path('int/<int:department_id>/', show_departments),
)