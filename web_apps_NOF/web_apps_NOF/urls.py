from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from disp_svodka.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('disp_svodka/', include('disp_svodka.urls', namespace='disp_svodka')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
