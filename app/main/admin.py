from django.contrib import admin
from django_mptt_admin.admin import MPTTModelAdmin, DjangoMpttAdmin
from django.utils.safestring import mark_safe
from .models import Product

import main.models as models


admin.site.site_title = 'Панель управления'
admin.site.site_header = 'Панель управления'
admin.site.index_title = 'Реми'


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent')
    list_display_links = ('title',)
    search_fields = ('title', 'parent__title')
    list_editable = ('parent',)
    list_filter = ('parent', 'title')

admin.site.register(models.Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'get_photo', 'category', 'promo')
    list_display_links = ('title',)
    search_fields = ('title', 'category__title', 'description', 'promo')
    list_editable = ('price', 'quantity', 'image', 'category', 'promo')
    list_filter = ('title', 'promo', 'price')
    fields = ('title', 'description', 'price', 'quantity', 'category', 'promo', 'image', 'get_photo', 'update')
    readonly_fields = ('update', 'get_photo')

    def get_photo(self, object: Product):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_photo.short_description = 'Фото'

admin.site.register(models.Product, ProductAdmin)




admin.site.register(models.Promo)
admin.site.register(models.Basket)
admin.site.register(models.Customer)

