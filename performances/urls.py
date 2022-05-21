from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.all_artists, name="artists"),
    path('performances/', views.all_performances, name="performances"),
    path('artists/<artist_id>', views.artist_page, name="artist_page"),
]
