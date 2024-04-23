from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm

def index(request):
    songs = Song.objects.all()
    if not songs:
        message = "No songs available."
    else:
        message = None
    return render(request, 'music_player/index.html', {'songs': songs, 'message': message})

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SongForm()
    return render(request, 'music_player/upload_song.html', {'form': form})

def play_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music_player/play_song.html', {'song': song})