from django.db import models


class Products(models.Model):
    name = models.CharField("name" , max_length=100)
    description = models.TextField("description" , max_length=3000)
    cost = models.PositiveSmallIntegerField("cost")
    status = models.CharField("status" , max_length=32)
    date = models.DateField()
    amount = models.PositiveSmallIntegerField("amount")
    icon = models.ImageField(upload_to='images/') 
    class Meta:
        db_table = 'products' 
