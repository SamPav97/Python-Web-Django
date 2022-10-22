from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstagram_project.common.urls')),
    path('accounts/', include('Petstagram_project.accounts.urls')),
    path('pets/', include('Petstagram_project.pets.urls')),
    path('photos/', include('Petstagram_project.photos.urls')),

]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    # '''
# After `startapp APP_NAME`
#
# 1. Create `APP_NAME/urls.py with empty `urlpatterns`
# 2. Include `APP_NAME/urls.py` into project's urls.py
# 3. ADD `APP_NAME` to `INSTALLED_APPS` in settings.py
# '''