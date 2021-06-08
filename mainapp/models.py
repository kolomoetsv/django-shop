from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Employee(models.Model):
    """
    Model representing a seller
    """
    first_name = models.CharField(max_length=50, verbose_name='Имя продавца', help_text="Введите имя продавца")
    last_name = models.CharField(max_length=50, verbose_name='Фамилия продавца', help_text="Введите фамилию продавца")

    # Methods
    def __str__(self):
        # String for representing the Model object.
        return 'Продавец {} {}'.format(self.last_name, self.first_name)


class Item(models.Model):
    """
    Model representing an item (product)
    """
    title = models.CharField(max_length=200, verbose_name='Наименование товара', help_text="Введите название товара")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание товара', help_text="Введите описание товара")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    # Methods
    def __str__(self):
        # String for representing the Model object.
        return self.title

    def get_absolute_url(self):
        # Returns the url to access a particular item instance.
        return reverse('item_detail', kwargs={'slug': self.slug})


class Sale(models.Model):
    """
    Model representing a sale
    """
    item = models.ForeignKey(Item, verbose_name='Наименование товара', on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee, verbose_name='Продавец')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    date_of_sale = models.DateTimeField(auto_now=True, verbose_name='Дата продажи')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    # Methods
    def save(self, *args, **kwargs):
        self.total_price = self.qty * self.item.price
        super().save(*args, **kwargs)

    def __str__(self):
        # String for representing the Model object.
        return self.item

