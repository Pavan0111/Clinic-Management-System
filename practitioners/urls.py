from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.practitioners, name='practitioners'),
    path("practitioners/", views.practitioners, name="practitioners"),
    path("add_practitioners/", views.add_practitioners, name="add_practitioners"),
    path("practitioners_details/<int:id>/", views.practitioners_details, name="practitioners_details"),
    path("edit_practitioners/<int:id>/", views.add_practitioners, name="edit_spractitioners"),
    
]