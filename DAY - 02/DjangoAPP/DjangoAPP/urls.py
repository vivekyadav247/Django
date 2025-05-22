
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('service/',views.service),
    path('login/',views.login),
    path('register/',views.register),
    path('contact/',views.contact),
]
