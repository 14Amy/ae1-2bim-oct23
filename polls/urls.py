from django.urls import path

from . import views

urlpatterns = [
    path("pais/", views.pais, name="pais"),
    path("barrio/", views.barrio, name="barrio"),
]