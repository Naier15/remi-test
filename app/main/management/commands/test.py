from turtle import title
from django.core.management.base import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = Product.objects.get(id=420).category.get_root()
        print(c)