# Generated by Django 5.1.1 on 2024-10-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
