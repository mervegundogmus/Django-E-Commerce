# Generated by Django 3.1 on 2020-08-23 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_shopcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='quantity',
            new_name='ay',
        ),
        migrations.RenameField(
            model_name='shopcart',
            old_name='quantity',
            new_name='ay',
        ),
    ]
