from multiprocessing import context
from django.shortcuts import render

from .models import Cat


def cats(request):
    cats = Cat.objects.all()
    context = {"cats": cats}
    return render(request, "cats/cats.html", context)


def cat(request, cat_id):
    return render(request, "cats/cat.html")


def search(request):
    return render(request, "cats/search.html")
