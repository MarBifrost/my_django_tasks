# Generated by Django 5.1.1 on 2024-10-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_category_sub_category_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, to='store.category'),
        ),
    ]
