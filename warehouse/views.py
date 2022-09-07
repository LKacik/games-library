from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def add(request):
    return render(request, 'add.html')


def remove(request):
    return render(request, 'remove.html')


def edit(request):
    return render(request, 'edit.html')


def search(request):
    return render(request, 'search.html')
