from django.shortcuts import render
from cats.models import Cat
from volunteers.models import Volunteer


def index(request):
    cats = Cat.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {"cats": cats}
    return render(request, "pages/index.html", context)


def about(request):
    volunteers = Volunteer.objects.all()
    context = {"volunteers": volunteers}
    return render(request, "pages/about.html", context)
