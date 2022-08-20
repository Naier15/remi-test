from django.core.management.base import BaseCommand
from random import randint, choice
from os import listdir, path
from django.conf import settings

from main.models import Category, Product
from main.utils import query_counter


def get_img(path_to_imgs: str) -> str:
    imgs: str = path.join(settings.BASE_DIR, path_to_imgs)
    result: str = choice(listdir(imgs))
    return path_to_imgs + result


class Command(BaseCommand):
    @query_counter
    def handle(self, *args, **kwargs):
        # Предварительно удаляем записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Добавляем категории
        category_lvl1 = ('Продукты', 'Напитки', 'Бытовая химия', 'Цветы')
        for cat in category_lvl1:
            Category.objects.create(title=cat)


        # Добавляем категории 2 уровня
        category_lvl2 = [['Фрукты', 'Мясо', 'Овощи', 'Гарниры'],
                         ['Молоко', 'Пиво', 'Соки', 'Вода'],
                         ['Отбеливатели', 'Стиральные порошки', 'Мыло', 'Ополаскиватели'],
                         ['Розы', 'Лилии', 'Ромашки', 'Хризантемы']]
        queries = []
        extra = {'level': 0, 'lft': 0, 'rght': 0, 'tree_id': 0}

        for i, category_lvl1 in enumerate(Category.objects.all()):
            query = [Category(title=subcategory, parent=category_lvl1, **extra)
                for subcategory in category_lvl2[i]]
            queries.extend(query)

        Category.objects.bulk_create(queries)
        Category.objects.rebuild()
        

        # Добавляем  продукты
        category_lvl2 = Category.objects.exclude(parent_id=None)
        length_of_categories = len(category_lvl2)
        phrases = ['сказка на яву', 'только у нас', 'выгодно', 'получается', 
                    'лучшее', 'за свои деньги', 'покупай скорее', 
                    'возьми скорее', 'и', 'только сегодня']
        path_to_imgs = r'static/photos/2022/08/17/'

        queries = [Product(title=f'Товар №{i}',
                         description=' '.join([choice(phrases) for _ in range(randint(5, 12))]).capitalize(),
                         price=randint(15000, 200000)/100,
                         quantity=randint(1, 100),
                         category=category_lvl2[i%length_of_categories],
                         image=get_img(path_to_imgs))
                for i in range(1, 81)]

        Product.objects.bulk_create(queries)
