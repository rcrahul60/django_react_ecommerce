# Generated by Django 3.1.7 on 2021-05-11 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210409_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='coutInStock',
            new_name='countInStock',
        ),
    ]
