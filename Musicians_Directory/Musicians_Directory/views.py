from django.shortcuts import render
from Albums.models import Album

def home(request):
    album_list = Album.objects.all()
    return render(request, 'home.html', {'data': album_list})