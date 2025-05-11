from django.urls import path

from cabins import views

app_name = 'cabins'

urlpatterns = [
    #path('search/', views.catalog, name='search'),
    path('', views.catalog, name='index'),
    path('cabin/<slug:cabin_slug>/', views.cabin, name='cabin'),
]


