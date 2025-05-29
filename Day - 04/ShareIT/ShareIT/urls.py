from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('service/',views.service),
    path('register/',views.register),
    path('login/',views.login),
    path('myadmin/',views.adminhome),
    path('user/',views.userhome),
    path('manageusers/',views.manageusers),
    path('manageuserstatus/',views.manageuserstatus),
    path('sharenotes/',views.sharenotes),
    path('viewnotes/',views.viewnotes),
    path('verify/', views.verify),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
