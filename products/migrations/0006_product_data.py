# Generated by Django 2.0.7 on 2018-07-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_nasc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]