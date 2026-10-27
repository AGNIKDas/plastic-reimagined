"""
URL configuration for Plastic Reimagined project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Administration (for staff moderation and content management)
    path('admin/', admin.site.urls),

    # Core Navigation & Vision
    path('', include('core.urls')),

    # Feature Applications
    path('studio/', include('studio.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
]

# Serve media files in local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
