from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, editable=False)  # Поле brand сделаем неизменяемым

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def p_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse('showcase:product', kwargs={'p_slug': self.slug})

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'


@receiver(pre_save, sender=Products)
def set_brand(sender, instance, **kwargs):
    if instance.category and instance.category.brand:
        instance.brand = instance.category.brand


class Images(models.Model):
    image = models.ImageField(blank=True, null=True)
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
