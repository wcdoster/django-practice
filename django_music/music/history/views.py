from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Artist, Song


def index(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'history/index.html', context)

# def song(request, artist_id):
#     song_list = Song.objects.all()
#     return render(request, 'history/song.html', )
    
def song(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/songs.html', {'artist': artist})