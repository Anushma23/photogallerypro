"""
URL configuration for PhotoGallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from PhotoGallery import settings
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show',views.showlist,name='list'),
    # path('view/<str:i1>',views.view,name='view1'),            full details shown
    path('photo/<str:pk>',views.PhotoFunction,name='photo'),
    # path('gallery',views.GalleryFunction,name='gallery'),
    path('upload',views.Uploadfunction,name='upd')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
