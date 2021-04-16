from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя продавца')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия продавца')

    def __str__(self):
        return 'Продавец {} {}'.format(self.last_name, self.first_name)


class Item(models.Model):
    employee = models.ManyToManyField(Employee, verbose_name='Продавец', through='Sale')
    title = models.CharField(max_length=200, verbose_name='Наименование товара')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Sale(models.Model):
    item = models.ForeignKey(Item, verbose_name='Наименование товара', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name='Продавец', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    date_of_sale = models.DateTimeField(auto_now=True, verbose_name='Дата продажы')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    def __str__(self):
        return self.item
