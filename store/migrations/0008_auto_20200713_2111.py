# Generated by Django 3.0.8 on 2020-07-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200712_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='pincode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]