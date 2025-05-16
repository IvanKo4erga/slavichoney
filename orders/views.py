import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from yookassa import Payment, Configuration
import json
import asyncio

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    total_price = 0
                    payment = form.cleaned_data['payment_on_get']

                    if cart_items.exists():

                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=payment,
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            total_price += quantity * price
                            print(name, quantity, price, total_price)
                            product.save()

                        print(payment)
                        if payment == '0':
                            idempotence_key = uuid.uuid4()

                            currency = 'RUB'
                            description = 'Товары в корзине'
                            payment = Payment.create({
                                "amount": {
                                    "value": str(total_price),
                                    "currency": currency
                                },
                                "confirmation": {
                                    "type": "redirect",
                                    "return_url": request.build_absolute_uri(reverse('orders:payment-success')),
                                },
                                "capture": True,
                                "test": True,
                                "description": description,
                            }, idempotence_key)

                            confirmation_url = payment.confirmation.confirmation_url

                            cart_items.delete()

                            messages.success(request, 'Заказ оформлен!')
                            return redirect(confirmation_url)

                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('users:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        phone_number = ''
        if request.user.phone_number:
            phone_number = request.user.phone_number
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': phone_number,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Славянский мед - Оформление заказа',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)


def payment_success(request):
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    return render(request, 'orders/payment-success.html')


def payment_failed(request):
    return render(request, 'orders/payment-failed.html')
