# Generated by Django 2.0.7 on 2018-07-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180707_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nasc',
            field=models.CharField(max_length=10, null=True),
        ),
    ]