from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail, BadHeaderError

import uuid
from fpdf import FPDF


class Peer(models.Model):
    idx = models.CharField('Идентификатор', max_length=150, default=uuid.uuid4)
    latitude = models.CharField('Широта', max_length=150)
    longitude = models.CharField('Долгота', max_length=150)
    city = models.CharField('Долгота', max_length=150)
    ip = models.CharField('Ip адрес', max_length=150, null=True, blank=True, default='')
    create_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    def __str__(self):
        return self.idx

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
        ordering = ['create_at']

    def save(self, *args, **kwargs):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.add_font('roboto', '', r'./static/fonts/Roboto-Black.ttf', uni=True)
        pdf.set_font('roboto', '', 12)
        pdf.write(5, f'Гость №{self.idx} - ip: {self.ip}')
        pdf.ln(10)
        pdf.write(5, f'Координаты: {self.latitude} - {self.longitude}')
        pdf.ln(10)
        pdf.write(5, f'Город: {self.city}')
        pdf.output(f"./static/data/docs/{self.idx}.pdf")
        super(Peer, self).save(*args, **kwargs)


def email_handler(sender, instance, created, **kwargs):
    print(f'[INFO] Registered another one connection from {instance.city}')
    # Uncomment to send_email. Also necessary to redefine DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL fields
    # try:
    #     send_mail(f'Оповещение от сервера', f'Registered another one connection from {instance.city}',
    #                 settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
    # except BadHeaderError:
    #     print(f'[ERROR] While send_email something went wrong')

post_save.connect(email_handler, sender=Peer)


class Category(MPTTModel):
    title = models.CharField('Категория', max_length=200, unique=True, default='')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True, default=None, verbose_name='Родительская категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

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
    description = models.TextField('Описание', blank=False, default=None, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=False, default=None, null=True)
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=1, blank=False, default=None, null=True)
    image = models.ImageField('Фотография', upload_to='static/photos/%Y/%m/%d', null=True, blank=True)
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True, default=None, verbose_name='Категория')
    promo = models.ForeignKey(Promo, on_delete=models.SET_NULL, null=True, default=None, blank=True, verbose_name='Акция')
    update = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['update']


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