from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
import uuid


class Category(MPTTModel):
    title = models.CharField('Категория', max_length=200, unique=True, default='')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True, default=None, verbose_name='Родительская категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    # class MPTTMeta:
    #     order_insertion_by = ['title']


    # def get_absolute_url(self):
    #     return reverse("category", kwargs={"pk": self.pk})
    


class Promo(models.Model):
    title = models.CharField('Название акции', max_length=300)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=300, db_index=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=False, default=None, null=True)
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=1, blank=False, default=None, null=True)
    image = models.ImageField('Фотография', upload_to='static/photos/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True, default=None, verbose_name='Категория')
    promo = models.ForeignKey(Promo, on_delete=models.SET_NULL, null=True, default=None, blank=True, verbose_name='Акция')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Customer(models.Model):
    name = models.CharField('Имя', max_length=120, blank=True, null=True, default=f'User-{id}')
    reg_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    profile = models.UUIDField(',, покупателя', default=uuid.uuid4, editable=False, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Basket(models.Model):
    ref_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='basket')
    ref_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField('Количество', default=0)
    datetime = models.DateTimeField('Дата покупки', auto_now_add=True)

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'