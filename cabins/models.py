from django.db import models
from django.urls import reverse


class Cabins(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')

    class Meta:
        db_table = 'cabin'
        verbose_name = 'Домик'
        verbose_name_plural = 'Домики'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price

# class Dates(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь",
#                              default=None)
#     cabin = models.ForeignKey(to=Cabin, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="домик",
#                              default=None)
#     date = models.DateField(verbose_name="дата бронирования")
#
#     class Meta:
#         db_table = 'date'
#         verbose_name = 'Даты'
#         verbose_name_plural = 'Даты'
