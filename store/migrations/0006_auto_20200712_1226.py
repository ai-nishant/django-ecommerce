# Generated by Django 3.0.8 on 2020-07-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200712_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]