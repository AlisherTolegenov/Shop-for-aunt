from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    img = models.ImageField(default='noimage.png', upload_to='product_image', verbose_name='Изображение подкатегории')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категории')
    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'
        ordering = ['name']
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена', db_index=True)
    availability = models.BooleanField(default=True, verbose_name='Наличие')
    img = models.ImageField(default='noimage.png', upload_to='product_image', verbose_name='Изображение')
    rating = models.IntegerField(null=True, blank=True, db_index=True, verbose_name='Популярность товара')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    subcategory = models.ForeignKey('SubCategory', null=True, on_delete=models.PROTECT, verbose_name='Подкатегория')
    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['rating']
