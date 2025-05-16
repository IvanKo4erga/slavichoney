from django.contrib import admin

from cabins.models import Cabins



@admin.register(Cabins)
class CabinsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "price", "discount"]
    list_editable = ["discount", ]
    search_fields = ["name", "description"]
    list_filter = ["discount"]
    fields = [
        "name",
        "slug",
        "description",
        "image",
        ("price", "discount"),
    ]
