from django.contrib import admin
from django.urls import path, include
#  todo: change temporary solution to something more permanent
from django.conf import settings
from django.conf.urls.static import static
from core.views import front, contact

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('homebrew/', include('homebrew.urls'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
