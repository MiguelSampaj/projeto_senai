from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default='', unique=True)
    user_email = models.EmailField(default='', unique=True)
    user_born_date = models.DateField(default='2000-01-01')
    user_key = models.CharField(max_length=20, default='')
    user_history = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f'ID: {self.user_id}, Name: {self.user_name}, Email: {self.user_email}'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default='')
    product_description = models.TextField(max_length=5000, default='')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_quantity = models.IntegerField(default=0)
    product_history = models.JSONField(default=dict, null=True, blank=True)
    product_image = models.CharField(max_length=500, default='', null=True, blank=True)

    def __str__(self):
        return f'ID: {self.product_id}, Name: {self.product_name}, Price: {self.product_price}, Quantity: {self.product_quantity}'
