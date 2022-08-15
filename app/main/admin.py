from django.contrib import admin
from django_mptt_admin.admin import MPTTModelAdmin, DjangoMpttAdmin

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
    list_display = ('title', 'price', 'quantity', 'image', 'category', 'promo')
    list_display_links = ('title',)
    search_fields = ('title', 'category__title')
    list_editable = ('price', 'quantity', 'image', 'category', 'promo')
    list_filter = ('title', 'promo', 'price')

admin.site.register(models.Product, ProductAdmin)




admin.site.register(models.Promo)
admin.site.register(models.Basket)
admin.site.register(models.Customer)

