# Generated by Django 5.0.1 on 2024-05-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_rename_city_books_1_last_name_remove_books_1_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_1',
            name='profile_image',
        ),
    ]
