from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def album(request):
    if request.method == 'POST':
        albums = AlbumForm(request.POST)
        if albums.is_valid():
            albums.save()
            return redirect('homepage')
    else:
        albums = AlbumForm()  
    return render(request, 'album.html', {'form': albums})

# edit album

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)

    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'album.html', {'form': album_form})

# delete album

def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')