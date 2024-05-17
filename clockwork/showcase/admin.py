from django.contrib import admin
from showcase.models import Categories, Products, Images, Brands


class BrandsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    exclude = ['slug']


class CategoriesAdmin(admin.ModelAdmin):
    exclude = ['slug']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'price', 'category']
    autocomplete_fields = ['brand']
    exclude = ['slug']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image']


admin.site.register(Brands, BrandsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Images, ImagesAdmin)
