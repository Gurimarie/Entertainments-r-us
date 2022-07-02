""" urls for app Performances """
from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.all_artists, name="artists"),
    path('performances/', views.all_performances, name="performances"),
    path('artists/artist_page/<int:pk>/', views.artist_page,
         name="artist_page1"),
    path('artists/artist_page/Artist: <artist_name>/', views.artist_page,
         name="artist_page2"),
    path('artists/artist_products/<int:pk>/', views.artist_products,
         name="artist_products"),
    path('artists/artist_details/<int:pk>/', views.artist_details,
         name="artist_details"),
    path('artists/artist_products/artist_product_details/<int:pk>/',
         views.artist_product_details, name="artist_product_details"),
]
