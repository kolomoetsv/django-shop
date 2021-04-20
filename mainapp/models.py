from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


class LatestProductsManager:

    @staticmethod
    def get_products_for_index_page(*args, **kwargs):
        #Method that returns last published items for the main page
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:4]
            products.extend(model_products)
        return products


class LatestProducts:

    objects = LatestProductsManager()


class Employee(models.Model):
    """
    Model representing a seller
    """
    first_name = models.CharField(max_length=50, verbose_name='Имя продавца', help_text="Введите имя продавца")
    last_name = models.CharField(max_length=50, verbose_name='Фамилия продавца', help_text="Введите фамилию продавца")

    def __str__(self):
        #String for representing the Model object.
        return 'Продавец {} {}'.format(self.last_name, self.first_name)


class Item(models.Model):
    """
    Model representing an item (product)
    """
    employee = models.ManyToManyField(Employee, verbose_name='Продавец', through='Sale')
    title = models.CharField(max_length=200, verbose_name='Наименование товара', help_text="Введите название товара")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание товара', help_text="Введите описание товара")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        #String for representing the Model object.
        return self.title

    def get_absolute_url(self):
        #Returns the url to access a particular item instance.
        return reverse('item_detail', args=[str(self.slug)])


class Sale(models.Model):
    """
    Model representing a sale
    """
    item = models.ForeignKey(Item, verbose_name='Наименование товара', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name='Продавец', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    date_of_sale = models.DateTimeField(auto_now=True, verbose_name='Дата продажы')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    def __str__(self):
        #String for representing the Model object.
        return self.item
