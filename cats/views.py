from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Cat


def cats(request):
    cats = Cat.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(cats, 6)
    page = request.GET.get('page')
    paged_cats = paginator.get_page(page)
    context = {"cats": paged_cats}
    return render(request, "cats/cats.html", context)


def cat(request, cat_id):
    return render(request, "cats/cat.html")


def search(request):
    return render(request, "cats/search.html")
