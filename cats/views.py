from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .choices import age_choices, gender_choices, donation_choices

from .models import Cat


def cats(request):
    cats = Cat.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(cats, 6)
    page = request.GET.get('page')
    paged_cats = paginator.get_page(page)
    context = {"cats": paged_cats}
    return render(request, "cats/cats.html", context)


def cat(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    context = {'cat':cat}
    return render(request, "cats/cat.html", context)


def search(request):
    context = {
        "age_choices": age_choices,
        "gender_choices": gender_choices,
        "donation_choices": donation_choices,
    }
    return render(request, "cats/search.html", context)
