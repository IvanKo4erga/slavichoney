from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_failed, name='payment-failed'),
]
