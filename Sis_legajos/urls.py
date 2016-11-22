"""Sis_legajos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Alumnos import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='Home'),
    url(r'^busqueda_dni/$', views.busqueda_dni),
    url(r'^busqueda_apellido/$', views.busqueda_apellido),
    url(r'^busqueda_legajo/$', views.busqueda_legajo),
    url(r'^legajo/([0-9]+)/$', views.alumno),
    url(r'^nuevo_alumno/$', views.nuevo_alumno),
    url(r'^almacenar/$', views.almacenar),
    url(r'^login/$',login,{'template_name':'login.html'}),
    url(r'^logout/$',logout,{'template_name':'logout.html'}),
]
