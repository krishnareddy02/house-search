# Generated by Django 5.0.1 on 2024-01-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_books_data1_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_data1',
            name='email',
            field=models.EmailField(default='null@gmail.com', max_length=254),
        ),
    ]
