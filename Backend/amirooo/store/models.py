from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    dics = HTMLField(blank=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'products/images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"
    
class ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    addition_price = models.IntegerField(default=0)
    file = models.FileField(upload_to=f'products/fiels/')

    def __str__(self):
        return f"{self.product.name} - File {self.title}"