from django.shortcuts import render
from .models import Games, AddGame
from .forms import PostForm
from .utils import add_new_game


def main(request):
    objs = Games.objects.all()
    return render(request, 'main.html', {'objs': objs})


def add(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        add_new_game(new_title)
    return render(request, 'add.html')


def remove(request):
    return render(request, 'remove.html')


def edit(request):
    return render(request, 'edit.html')


def search(request):
    return render(request, 'search.html')
