# Generated by Django 5.1.1 on 2024-10-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_sub_category_category_parents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parents',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='parents',
            new_name='subcategory',
        ),
    ]
