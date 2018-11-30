from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.customer_id

class Product(models.Model):
    product_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.product_id


class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    order_id = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    value = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    order_date = models.DateTimeField()

    def __unicode__(self):
        return self.order_id

class SalesDetails(models.Model):
    order_id = models.CharField(max_length=200)
    order_date = models.DateTimeField()
    customer_id = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    product_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)


    def __unicode__(self):
        return self.order_id