from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'productCategory'
        verbose_name_plural = 'productCategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='store')
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name