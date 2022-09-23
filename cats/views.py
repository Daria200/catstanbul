from django.shortcuts import render


def cats(request):
    return render(request, "cats/cats.html")


def cat(request):
    return render(request, "cats/cat.html")


def search(request):
    return render(request, "cats/search.html")
