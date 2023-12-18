from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
def musician_list(request):
    if request.method == 'POST':
        musician = MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            return redirect('musician')
    else:
        musician = MusicianForm()
    return render(request, 'musician.html', {'form': musician})

# edit misician data

def edit_musician(request,id):
    musician_detail= Musician.objects.get(pk=id)
    musician_lst = MusicianForm(instance=musician_detail)

    if request.method == 'POST':
        musician_lst = MusicianForm(request.POST, instance=musician_detail)
        if musician_lst.is_valid():
            musician_lst.save()
            return redirect('homepage')
    return render(request, 'musician.html', {'form':musician_lst})