from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ('title',)

class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id', 'title', 'amount', 'price', 'active']
    list_display_links = ['title', 'amount', 'price', 'active']
    search_fields = ('title',)

class CategoryAdmin(MPTTModelAdmin):
    readonly_fields = ('id',)
    list_display = ['id','title']
    list_display_links = ['title']
    search_fields = ('title',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, MPTTModelAdmin)