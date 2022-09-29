from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from volunteers.models import Volunteer


class Cat(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    donation = models.IntegerField()
    age = models.IntegerField()
    vaccinated = models.BooleanField(default=True)
    gender_choices = [("male", "male"), ("female", "female")]
    gender = models.CharField(max_length=10, choices=gender_choices)
    breed = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    available_from = models.DateField(default=datetime.now, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
