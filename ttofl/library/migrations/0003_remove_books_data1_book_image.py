# Generated by Django 5.0.1 on 2024-01-24 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_profile_image_books_data1_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_data1',
            name='book_image',
        ),
    ]
