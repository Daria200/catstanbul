from django.urls import path
from . import views

urlpatterns = [
    path("", views.cats, name="cats"),
    path("<int:cat_id>", views.cat, name="cat"),
    path("search", views.search, name="search"),
]
