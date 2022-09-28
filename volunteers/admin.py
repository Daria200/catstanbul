from django.contrib import admin
from .models import Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_vom", "phone", "email")
    list_display_links = ("id", "name")
    list_editable = ("is_vom",)
    search_fields = ("name", "description", "phone", "email")
    list_per_page = 25


admin.site.register(Volunteer, VolunteerAdmin)
