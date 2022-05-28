from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key = True)
    shop = models.ManyToManyField('Shop')
    description = models.ManyToManyField('Category')
    title = models.CharField(max_length = 255)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    images = models.ImageField(upload_to='Product_images/', null=True, blank=True)
    active = models.BooleanField(default=False, null=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

    def __str__(self):
        return self.title

class Category(MPTTModel):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=255)
    description = models.ManyToManyField('Product', blank = True, related_name = 'category_products')
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, default=None)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Shop(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.ManyToManyField('Product', related_name='shop_products', blank = True)
    imageUrl = models.ImageField(upload_to='shop_photos/', null=True, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['title']

    def __str__(self):
        return self.title