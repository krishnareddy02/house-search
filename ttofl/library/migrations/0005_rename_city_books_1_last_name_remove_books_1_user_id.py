# Generated by Django 5.0.1 on 2024-05-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_books_data1_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books_1',
            old_name='city',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='books_1',
            name='user_id',
        ),
    ]
