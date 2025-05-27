from django.contrib import admin
from django.urls import path


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
]
