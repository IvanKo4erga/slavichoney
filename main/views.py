# from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products


# from django.views.generic import TemplateView
#
# from goods.models import Categories


def index(request):
    goods = Products.objects.filter(discount__gt=0)[:6]
    context = {
        'title': 'Славянский мед - Главная',
        'goods': goods,
        # 'content': 'Магазин пчеловодческой продукции "Славянский мед"',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Славянский мед - О нас',
        # 'content': "О нас",
        # 'text_on_page': "Наша пасека расположилась в тихом живописном уголке Ульяновской области - поселке Борисовка "
        #                 "Чердаклинского района. Здесь есть все, чем очаровывает и славится природа Поволжья: "
        #                 "разнотравье цветущих лугов, ягодные холмы, грибные леса и просторы полей.."
    }
    return render(request, 'main/about.html', context)
