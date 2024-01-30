from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    dics = HTMLField(blank=True)

    def calculate_total_price(self):
        selected_product_types = self.product_types.filter(select=True)
        total_addition_price = sum(product_type.addition_price for product_type in selected_product_types)
        return self.price + total_addition_price
    
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'products/images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"
    
class ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_types')
    title = models.CharField(max_length=200)
    addition_price = models.IntegerField(default=0)
    file = models.FileField(upload_to=f'products/fiels/')
    select = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - File {self.title}"