"""
URL configuration for bar_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cardapio import views_db_files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardapio.urls')),
    # Compat: serve files stored in DB without relying on package's old URLs
    path('files/get/', views_db_files.get_file, kwargs={"add_attachment_headers": False}, name='db_file_storage.get_file'),
    path('files/download/', views_db_files.get_file, kwargs={"add_attachment_headers": True}, name='db_file_storage.download_file'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
