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
    path('add_artist/', views.add_artist, name="add_artist"),
    path('add_performance/', views.add_performance, name="add_performance"),
    path('add_artist_product/', views.add_artist_product,
         name="add_artist_product"),
]
