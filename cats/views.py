from ast import keyword
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
    queryset_list = Cat.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
    # Gender
    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list = queryset_list.filter(gender__iexact = gender)
    
    # Age
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            queryset_list = queryset_list.filter(age__iexact = age)
    
    # Donation
    if 'donation' in request.GET:
        donation = request.GET['donation']
        if donation:
            queryset_list = queryset_list.filter(donation__iexact = donation)


    context = {
        "age_choices": age_choices,
        "gender_choices": gender_choices,
        "donation_choices": donation_choices,
        'cats':queryset_list
    }
    return render(request, "cats/search.html", context)
