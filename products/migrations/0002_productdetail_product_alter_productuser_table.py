# Generated by Django 4.0.3 on 2022-04-10 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='productuser',
            table='productsusers',
        ),
    ]
