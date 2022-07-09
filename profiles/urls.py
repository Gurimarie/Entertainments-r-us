from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_profile, name="customer_profile"),
]
