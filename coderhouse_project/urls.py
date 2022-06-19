"""coderhouse_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path, include
from home.views import Error404View, Error505View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('software/', include('software.urls')),
    path('discussion/', include('discussion.urls')),
    path('hardware/', include('hardware.urls')),
    path('gaming/', include('gaming.urls')),
    path('user/', include('user.urls')),
]

if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404View.as_view()
handler500 = Error505View.as_error_view()

