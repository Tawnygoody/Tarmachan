# Generated by Django 3.2.7 on 2021-09-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='spec1',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec2',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec3',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec4',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]