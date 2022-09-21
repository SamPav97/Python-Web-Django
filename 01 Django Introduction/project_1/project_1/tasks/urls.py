from django.urls import path

from project_1.tasks.views import show_all_tasks, index

urlpatterns = (
    path('/', index),
    path('/all/', show_all_tasks),
)
