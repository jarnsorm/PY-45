from django.contrib import admin

from showcase.models import Categories, Products, Images


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'category']


admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Images)