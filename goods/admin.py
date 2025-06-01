import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount", ]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]

    # def changelist_view(self, request, extra_context=None):
    #     chart_data = (
    #         Products.objects.annotate(date=TruncDay("created_timestamp"))
    #         .values("date")
    #         .annotate(y=Count("id"))
    #         .order_by("-date")
    #     )
    #
    #     as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    #     extra_context = extra_context or {"chart_data": as_json}
    #
    #     return super().changelist_view(request, extra_context=extra_context)
