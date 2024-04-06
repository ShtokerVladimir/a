from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from prototype import views


urlpatterns = [
    path('', include('frontend.urls')),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
