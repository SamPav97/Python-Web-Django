from django.urls import path, include

from Musify.web.views import index, add_album, edit_album, delete_album, details_profile, delete_profile, details_album

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/<int:pk>/', details_profile, name='details profile'),
        path('delete/<int:pk>/', delete_profile, name='delete profile'),
    ])),
)
