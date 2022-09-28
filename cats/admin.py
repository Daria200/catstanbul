from django.contrib import admin
from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_published", "donation", "volunteer")
    list_display_links = ("id", "name")
    list_filter = ("volunteer",)
    list_editable = ("is_published",)
    search_fields = ("name", "description", "address", "city", "donation")
    list_per_page = 25


admin.site.register(Cat, CatAdmin)
