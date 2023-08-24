from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('songs/', views.song_list, name='song_list'),
    path('albums/', views.album_list, name='album_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('contact/', views.contact, name='contact'),
    path('policy/', views.policy, name='privacy-policy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('about/', views.about, name='About Us'),

]
