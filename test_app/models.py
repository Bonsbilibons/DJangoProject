from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser


class Categories(models.Model):
    name = models.CharField("name" , max_length=100)
    class Meta:
        db_table = 'categories'


class Products(models.Model):
    name = models.CharField("name" , max_length=100)
    description = models.TextField("description" , max_length=3000)
    cost = models.PositiveSmallIntegerField("cost")
    status = models.PositiveSmallIntegerField("status")
    amount = models.PositiveSmallIntegerField("amount")
    icon = models.CharField("icon" , max_length=50)
    category = models.ForeignKey(Categories , on_delete=models.CASCADE)
    created_at = models.DateTimeField("created_at")
    updated_at = models.DateTimeField("updated_at")
    class Meta:
        db_table = 'products' 
        

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'


class Reviews(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.TextField("title" , max_length = 120 )
    comment = models.TextField("comment" , max_length = 1250 )
    created_at = models.DateTimeField("created_at")
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    class Meta:
        db_table = 'comments'

class Purchases(models.Model):
    purch_id = models.CharField("purch_id" , max_length=50)
    total_sum = models.PositiveIntegerField("total_sum")
    payment_id = models.CharField("payment_id" , max_length=50)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField("status")
    created_at = models.DateTimeField("created_at")
    updated_at = models.DateTimeField("updated_at")

    class Meta:
        db_table = 'purchases' 

class Purchase_products(models.Model):
    purchase = models.ForeignKey(Purchases , on_delete=models.CASCADE)
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField("amount")
    created_at = models.DateTimeField("created_at")
    updated_at = models.DateTimeField("updated_at")
    class Meta:
        db_table = 'purchase_products'

class Payments(models.Model):
    purchase = models.ForeignKey(Purchases , on_delete=models.CASCADE)
    card = models.PositiveBigIntegerField("card")
    email = models.EmailField("email")
    created_at = models.DateTimeField("created_at")
    updated_at = models.DateTimeField("updated_at")
    class Meta:
        db_table = 'payments'