# Generated by Django 5.1 on 2024-12-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookshopaccount',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, related_name='borrowed_books', to='book.book'),
        ),
    ]
