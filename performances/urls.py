from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.all_artists, name="artists"),
    path('performances/', views.all_performances, name="performances"),
    path('artist_page/<int:pk>/', views.artist_page, name="artist_page"),
    path('artist_products/<int:pk>/', views.artist_products, name="artist_products"),
]
