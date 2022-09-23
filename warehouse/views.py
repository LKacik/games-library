from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, UpdateView

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


class Delete(DeleteView):
    model = Games
    success_url = reverse_lazy('main')
    template_name = 'remove.html'


class SingleView(DetailView):
    model = Games
    template_name = 'single.html'
    context_object_name = 'game'


class EditView(UpdateView):
    model = Games
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('main')


def edit(request):
    return render(request, 'edit.html')


def search(request):
    return render(request, 'search.html')
