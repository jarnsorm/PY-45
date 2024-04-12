from django.contrib import admin

from showcase.models import Categories, Products, Images


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'category']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image']


admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Images, ImagesAdmin)
