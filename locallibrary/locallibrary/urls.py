"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# importamos la vista de nuestra app catalog
from catalog.views import index_general

urlpatterns = [
    path('admin/', admin.site.urls),
    # castellanizar url catálogo
    path('catalogo/', include('catalog.urls')), 
    ## para el index general
    path('', index_general, name='index_general'),
    # para el debug_toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]






