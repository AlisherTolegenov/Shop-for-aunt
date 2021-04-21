from django.contrib import admin
from .models import Product, SubCategory, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'img', 'published', 'rating', 'subcategory')
    list_display_links = ('title', 'rating', 'subcategory')
    search_fields = ('title', 'rating', 'subcategory__name')



admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory)
admin.site.register(Category)


