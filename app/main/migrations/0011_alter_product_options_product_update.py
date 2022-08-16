# Generated by Django 4.1 on 2022-08-16 19:05

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['update'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now(), verbose_name='Дата добавления'),
            preserve_default=False,
        ),
    ]
