from django.db import models
from users.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f'{self.product.name}\'s image {self.id} '


class OrderItem(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f'{self.product.name}\'s order'


class Order(models.Model):
    item = models.ManyToManyField(OrderItem)
    made_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order by {self.item.customer.firstname}'

