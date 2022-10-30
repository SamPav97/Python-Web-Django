from django.urls import path, include

from CarApp.web.views import index, add_car, details_car, edit_car, delete_car, add_profile, details_profile, \
    delete_profile, edit_profile, catalogue

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('add/', add_car, name='add car'),
        path('details/<int:pk>/', details_car, name='details car'),
        path('edit/<int:pk>/', edit_car, name='edit car'),
        path('delete/<int:pk>/', delete_car, name='delete car'),
    ])),
    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
