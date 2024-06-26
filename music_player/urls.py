from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('upload/', views.upload_song, name='upload_song'),
    path('play/<int:song_id>/', views.play_song, name='play_song'), 
]