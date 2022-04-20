from django.db import models
from utils.timestamp import TimeStampedModel
from users.models import User, Seller

class Product(TimeStampedModel):
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    amount = models.IntegerField()
    goal_amount = models.IntegerField()
    end_date = models.DateTimeField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through="ProductUser")

    class Meta:
        db_table = "products"

class ProductUser(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "productsusers"

class Productdetail(models.Model):
    total_amount = models.IntegerField()
    total_supporter = models.IntegerField()
    rate = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "productdetails"