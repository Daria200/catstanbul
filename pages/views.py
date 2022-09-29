from django.shortcuts import render
from cats.models import Cat


def index(request):
    cats = Cat.objects.order_by('-list_date').filter(is_published=True)[1:4]
    context = {"cats": cats}
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")
