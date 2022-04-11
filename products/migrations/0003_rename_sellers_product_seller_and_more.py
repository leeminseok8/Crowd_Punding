# Generated by Django 4.0.3 on 2022-04-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productdetail_product_alter_productuser_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sellers',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='users',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
