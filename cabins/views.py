from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from cabins.models import Cabins


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    
    cabins = Cabins.objects.all()
    if not cabins.exists():
        raise Http404()

    if on_sale:
        cabins = cabins.filter(discount__gt=0)

    if order_by and order_by != "default":
        cabins = cabins.order_by(order_by)

    paginator = Paginator(cabins, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Славянский мед - Домики",
        "cabins": current_page,
        "slug_url": category_slug
    }
    return render(request, "cabins/catalog.html", context)


def cabin(request, cabin_slug):
    cabin = Cabins.objects.get(slug=cabin_slug)

    context = {"cabin": cabin}

    return render(request, "cabins/cabin.html", context)
