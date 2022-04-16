import os
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanted_pre_onboarding.settings")
django.setup()

from users.models  import User, Seller
from products.models import Productdetail, Product, ProductUser

SELLER_PATH = "./csv/seller.csv"
USER_PATH = "./csv/user.csv"
PRODUCT_PATH = "./csv/product.csv"
PRODUCTDETAIL_PATH = "./csv/productdetail.csv"
PRODUCTUSER_PATH = "./csv/productuser.csv"


def insert_seller():
    with open(SELLER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name = row[0]
            Seller.objects.create(name = name)
    print("SECCESSED UPLOAD SELLER DATA!")
    
def insert_user():
    with open(USER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            name = row[0]

            User.objects.create(name = name)
    print("SECCESSED UPLOAD USER DATA!")
    
def insert_product():
    with open(PRODUCT_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            subject = row[0]
            description = row[1]
            amount = row[2]
            goal_amount = row[3]
            end_date = row[4]
            seller_id = row[5]
            seller = Seller.objects.get(id=seller_id)

            Product.objects.create(
                subject = subject,
                description = description,
                amount = amount,
                goal_amount = goal_amount,
                end_date = end_date,
                seller = seller
            )
    print("SECCESSED UPLOAD PRODUCT DATA!")
    
def insert_productdetail():
    with open(PRODUCTDETAIL_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            total_amount = row[0]
            total_supporter = row[1]
            rate = row[2]
            product_id = row[3]
            product = Product.objects.get(id=product_id)

            Productdetail.objects.create(
                total_amount = total_amount,
                total_supporter = total_supporter,
                rate = rate,
                product = product
            )
    print("SECCESSED UPLOAD PRODUCTDETAIL DATA!")
    
def insert_productuser():
    with open(PRODUCTUSER_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            count = row[0]
            product_id = row[1]
            user_id  = row[2]
            product = Product.objects.get(id=product_id)
            user  = User.objects.get(id=user_id)

            ProductUser.objects.create(
                count = count,
                product = product,
                user = user
            )
    print("SECCESSED UPLOAD PRODUCTUSER DATA!")


insert_seller()
insert_user()
insert_product()
insert_productdetail()
insert_productuser()